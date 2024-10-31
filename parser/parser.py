import aiohttp
from bs4 import BeautifulSoup # type: ignore

class BaseParser:
    def __init__(self,
                 url:str,
                 headers:dict[str,str] = {'User-Agent': 'Mozilla/5.0'}
                 ) -> None:
        
        self.url:str = url
        self.headers:dict = headers 
    
    async def fetch(self, endpoint: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(f'{self.url}/{endpoint}') as response:
                data = await response.text() 
                return BeautifulSoup(data,  'html.parser')


class HTMLParser(BaseParser):
    def get_data(self,
                 soup: BeautifulSoup, 
                 tag: str, 
                 tag_class: str = "",
                 tag_id:str = ""
                 ) -> str:
        
        if tag_class: return soup.find_all(f'{tag}',{'class': f'{tag_class}'})
        if tag_id: return soup.find_all(f'{tag}',{'id': f'{tag_class}'})
        
        return soup.find_all(f'{tag}')
    
    def strip(self, soup: BeautifulSoup) -> list:
        strip_data = [] 
        for el in soup:
            strip_data.append(el.text.strip())
        return strip_data
    
    def check_enclosure(self, ):
        pass