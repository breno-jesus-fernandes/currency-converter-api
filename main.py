from fastapi import FastAPI
import httpx
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Conversion(BaseModel):
    real: float
    dolar: float
    euro: float


@app.get('convertemoeda/{valor_real}', response_model=Conversion)
async def converte_moeda(valor_real: float):
    rates = {'USD': 5.6, 'EUR': 6.2}

    valor_dolar = valor_real * rates['USD']
    valor_euro = valor_real * rates['EUR']

    return {
        'real': valor_real,
        'dolar': valor_dolar,
        'euro': valor_euro
    }

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)