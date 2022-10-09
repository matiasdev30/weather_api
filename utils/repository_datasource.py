import requests

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_status(city: str) -> requests.models.Response:
    """Method to get to get the html page of google with climate data"""
    try:
        city=city.replace(" ","+")
        city=city+" weather"
        res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
        return res
    except requests.exceptions.RequestException as e:
        print(e)

