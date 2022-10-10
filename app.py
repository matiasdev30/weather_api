from fastapi import FastAPI
from repository import scrappy_data
from modules import CityModel

app = FastAPI()

@app.get('/')
def index():
    return {'log':'weather[API]'}

@app.post('/get_city_weather')
def get_city_weather(city: str) -> CityModel:
    data = scrappy_data(city=city)
    city = CityModel(nome = data['location'], date=data['time'], statu=data['info'], temperatur=data['weather'])
    return city
