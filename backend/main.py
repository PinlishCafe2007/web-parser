from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from bs4 import BeautifulSoup
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

@app.get("/parse")
async def parse_url(url: str):
    connection = sqlite3.connect('WebParser.db')
    try:
        cursor = connection.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY,
            url TEXT UNIQUE
        )''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS titles (
            id INTEGER PRIMARY KEY,
            title TEXT,
            url_id INTEGER,
            FOREIGN KEY (url_id) REFERENCES urls(id)
        )''')

        cursor.execute("SELECT id FROM urls WHERE url = ?", (url,))
        url_row = cursor.fetchone()

        if url_row:
            url_id = url_row[0]
            cursor.execute("SELECT title FROM titles WHERE url_id = ?", (url_id,))
            titles = [row[0] for row in cursor.fetchall()]
            return {"url": url, "titles": titles, "source": "database (cached)"}
        else:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            titles = [tag.get_text().strip() for tag in soup.find_all(['h1', 'h2', 'h3'])]

            cursor.execute("INSERT INTO urls (url) VALUES (?)", (url,))
            url_id = cursor.lastrowid
            
            for title in titles:
                cursor.execute("INSERT INTO titles (title, url_id) VALUES (?, ?)", (title, url_id))
            
            connection.commit()
            return {"url": url, "titles": titles, "source": "parsed (live)"}

    except Exception as e:
        return {"error": str(e)}
    finally:
        connection.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)