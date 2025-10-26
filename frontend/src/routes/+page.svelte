<script>
 let url="https://example.com"
 let titles=[]
 let loading=false

 async function parseUrl(){
  loading=true
  const res=await fetch(`http://localhost:8000/parse?url=${url}`)
  const data=await res.json()
  titles=data.titles
  loading=false
 }
</script>

<div class="container">
 <div class="header">
  <h1>📄 Парсер заголовков</h1>
  <p>Получите все заголовки h1-h3 с любого сайта</p>
 </div>
 
 <div class="controls">
  <input bind:value={url} placeholder="Введите URL сайта" class="url-input">
  <button on:click={parseUrl} disabled={loading} class="parse-btn">
   {loading?'⏳ Парсинг...':'🚀 Парсить'}
  </button>
 </div>

 {#if titles.length>0}
  <div class="results">
   <div class="results-header">
    <h2>Найдено заголовков: {titles.length}</h2>
    <span class="badge">✨ Готово</span>
   </div>
   <div class="titles">
    {#each titles as title,i}
     <div class="title-item">
      <span class="number">{i+1}.</span>
      <span class="text">{title}</span>
     </div>
    {/each}
   </div>
  </div>
 {:else if !loading}
  <div class="empty">
   <div class="empty-icon">🔍</div>
   <p>Введите URL и нажмите "Парсить"</p>
  </div>
 {/if}
</div>

<style>
 .container{max-width:600px;margin:40px auto;padding:0 20px;font-family:'Segoe UI',Arial,sans-serif}
 .header{text-align:center;margin-bottom:40px}
 h1{color:#2c3e50;margin-bottom:8px;font-size:2.2em}
 .header p{color:#7f8c8d;font-size:1.1em}
 .controls{display:flex;gap:12px;margin-bottom:30px}
 .url-input{flex:1;padding:14px;border:2px solid #bdc3c7;border-radius:8px;font-size:16px;transition:border-color 0.3s}
 .url-input:focus{outline:none;border-color:#3498db}
 .parse-btn{padding:14px 28px;background:linear-gradient(135deg,#3498db,#2980b9);color:white;border:none;border-radius:8px;cursor:pointer;font-size:16px;font-weight:600;transition:transform 0.2s}
 .parse-btn:hover:not(:disabled){transform:translateY(-2px)}
 .parse-btn:disabled{opacity:0.6;cursor:not-allowed;transform:none}
 .results{background:#ecf0f1;padding:24px;border-radius:12px;border-left:4px solid #3498db}
 .results-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:20px}
 .results h2{margin:0;color:#2c3e50;font-size:1.3em}
 .badge{background:#2ecc71;color:white;padding:6px 12px;border-radius:20px;font-size:0.9em;font-weight:500}
 .title-item{display:flex;align-items:flex-start;gap:12px;padding:12px 0;border-bottom:1px solid #bdc3c7;transition:background-color 0.2s}
 .title-item:hover{background:rgba(255,255,255,0.5);padding-left:8px;padding-right:8px;margin:0 -8px;border-radius:6px}
 .title-item:last-child{border-bottom:none}
 .number{color:#7f8c8d;font-weight:600;min-width:25px}
 .text{color:#2c3e50;line-height:1.4}
 .empty{text-align:center;padding:60px 20px;color:#95a5a6}
 .empty-icon{font-size:3em;margin-bottom:16px;opacity:0.7}
</style>