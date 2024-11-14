import './App.css'


function App() {  
  return (
    <>
    <h1>Huffman Archiver</h1>
    <div className="forms-container">
        <form encType="multipart/form-data" method="post" action="http://localhost:8000/encode">
            <p>
                <input type="file" name="file" />
            </p>
            <p>
                <input className='btn' type="submit" value="Сжать файл" />
            </p>
        </form>

        <form encType="multipart/form-data" method="post" action="http://localhost:8000/decode">
            <p>
                <input type="file" name="file" />
            </p>
            <p>
                <input className='btn' type="submit" value="Извлечь" />
            </p>
        </form>
    </div>

    </>)
  }

export default App
