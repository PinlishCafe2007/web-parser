# 🌐 Web Parser

Умный парсер заголовков веб-страниц с кэшированием результатов в базе данных.

## 🚀 Особенности

- **📊 Парсинг заголовков** h1-h3 с любых веб-страниц
- **💾 Интеллектуальное кэширование** - повторные запросы выполняются мгновенно
- **🎯 Простой API** - один endpoint для всех операций
- **⚡ Быстрая работа** благодаря SQLite и эффективному парсингу

## 🛠 Технологии

- **Backend**: FastAPI, Python, BeautifulSoup4
- **Frontend**: Svelte, JavaScript
- **База данных**: SQLite с реляционной структурой
- **Парсинг**: HTML-парсинг с обработкой ошибок

## 📡 API Документация

### `GET /parse`
Парсит заголовки с указанного URL

**Параметры:**
- `url` (string) - URL для парсинга

**Пример запроса:**
http
GET http://localhost:8000/parse?url=https://example.com
Ответ:

{
  "url": "https://example.com",
  "titles": ["Example Domain", "This domain is for use..."],
  "source": "parsed (live)"
}

# 🏃‍♂️ Быстрый старт
Установка и запуск

## Клонировать репозиторий
git clone https://github.com/PinlishCafe2007/web-parser.git
cd web-parser

## Установить зависимости
pip install -r requirements.txt

## Запустить сервер
python main.py
## Запуск фронтенда
cd frontend
npm install
npm run dev


# 🎯 Использование
Запустите бэкенд и фронтенд

Откройте http://localhost:5173

Введите URL в поле ввода

Нажмите "Парсить" для получения заголовков

### 📄 Лицензия
MIT License
