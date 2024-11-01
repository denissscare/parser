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
                 tag_id:str = "",
                 ) -> str | list:
        
        if tag_class: return self._get_class_data(soup=soup, tag=tag, tag_class=tag_class)
        if tag_id: return self._get_id_data(soup=soup, tag=tag, tag_id=tag_id)
        
        return soup.find_all(f'{tag}')
    
    def strip(self, soup: BeautifulSoup) -> str:
        strip_data = [] 
        for el in soup:
            strip_data.append(el.text.strip())
        return " ".join(el.text.strip() for el in soup)
    
    
    def _get_href(self, link: BeautifulSoup) -> str:
        return link.get('href')
    
    
    def _get_class_data(self,
                        soup: BeautifulSoup,
                        tag: str,
                        tag_class: str) -> list:
        
        return soup.find_all(f'{tag}',{'class': f'{tag_class}'})
    
    def _get_id_data(self,
                     soup: BeautifulSoup,
                     tag: str,
                     tag_id: str) -> list:
        
        return soup.find_all(f'{tag}',{'id': f'{tag_id}'})
    
    def check_enclosure(self, ):
        pass