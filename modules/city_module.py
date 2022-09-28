from xmlrpc.client import DateTime
from pydantic import BaseModel

class CityModel(BaseModel):
    nome: str
    date: str
    statu: str
    temperatur: str
