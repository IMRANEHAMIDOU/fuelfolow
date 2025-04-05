from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

class Station(BaseModel):
    id: int
    name: str
    price_essence: float
    price_diesel: float

# Initialisation du tableau avec quelques stations
stations = [
    Station(id=1, name="Total Energies", price_essence=500, price_diesel=600),
    Station(id=2, name="Shell", price_essence=300, price_diesel=350),
    Station(id=3 , name="BP", price_essence=499.0, price_diesel=640)
]

@app.post('/stations/')
def create_station(station: Station):
    stations.append(station)
    return stations

@app.get('/stations/')
def get_stations():
    return stations