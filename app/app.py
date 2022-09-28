from symbol import import_stmt
from fastapi import FastAPI
import sample.repository

app = FastAPI()

@app.get('/')
def index():
    return {'log':'weather[API]'}

@app.post('/get_city_weather')
def get_city_weather(city: str):
    data = scrappy_data(city=city)
    return data



