from fastapi.params import File
from fastapi import status
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from typing import Annotated, Union
from .api import encrypt,decrypt
from fastapi import FastAPI, Request, Response, UploadFile

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'PUT', 'DELETE'],
    allow_headers=["*"]
)

ITEMS = {}


@app.post("/encode")
def read_root(req:Request, file: bytes = File()):
    if(file == None):
      return
    
    encrypt(file)
    return FileResponse(path='Encoded.txt', filename='Закодированная строка.txt', media_type='multipart/form-data')


@app.post("/decode")
def upload_file_bytes(file: bytes = File()):
    if(file == None):
      return
    
    decrypt(file)
    return FileResponse(path='Decoded.txt', filename='Раскодированная строка.txt', media_type='multipart/form-data')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
