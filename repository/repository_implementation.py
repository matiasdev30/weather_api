from bs4 import BeautifulSoup 
from .repository_datasource import get_status

def scrappy_data(city: str) -> map:
    """Scrappy os dados"""
    data = {}
    soup = BeautifulSoup(get_status(city=city).text, 'html.parser')
    data['location'] = soup.select('#wob_loc')[0].getText().strip()
    data['time'] = soup.select('#wob_dts')[0].getText().strip()
    data['info'] = soup.select('#wob_dc')[0].getText().strip()
    data['weather'] = soup.select('#wob_tm')[0].getText().strip() + '°C'
    return data 