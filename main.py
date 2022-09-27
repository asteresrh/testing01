from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class mahasiswa(BaseModel):
    NIM: float
    Nama: str

@app.post("/data mahasiswa/")
def dataMahasiswa(dataMhs: mahasiswa):
    return dataMhs
    