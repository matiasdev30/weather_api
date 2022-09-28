from bs4 import BeautifulSoup 
from repository import get_status

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def scrappy_data(city: str) -> map:
    """Scrappy os dados"""
    data = {}
    soup = BeautifulSoup(get_status(city=city).text, 'html.parser')
    data['location'] = soup.select('#wob_loc')[0].getText().strip()
    data['time'] = soup.select('#wob_dts')[0].getText().strip()
    data['info'] = soup.select('#wob_dc')[0].getText().strip()
    data['weather'] = soup.select('#wob_tm')[0].getText().strip()
    return data
