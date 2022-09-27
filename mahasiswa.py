from http.client import HTTPException
import json
from fastapi import FastAPI

with open("Datamhs.json", "r") as read_file:
    data = json.load(read_file)

app = FastAPI()

@app.get('/DataMHS/{nimMHS}')
async def read_DataMHS(nimMHS: int):
    for mahasiswa in data['DataMHS']:
        if mahasiswa['NIM'] == nimMHS:
            return mahasiswa
    raise HTTPException(
        status_code=404, detail=f'Tidak ada mahasiswa'
    )