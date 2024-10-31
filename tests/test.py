from parser.parser import BaseParser, HTMLParser
import asyncio
from bs4 import BeautifulSoup # type: ignore

if __name__ == '__main__':
    pars = HTMLParser(url='https://quotes.toscrape.com')
    data = asyncio.run(pars.fetch('/'))
    
    pars_data = pars.get_data(data, 'div', 'quote')
    
    for e in pars_data:
        author = pars.get_data(e, 'small', 'author')
        print(*pars.strip(author))
        
        quote = pars.get_data(e, 'span', 'text')
        print(*pars.strip(quote))
        
        tags = pars.get_data(e, 'a', 'tag')
        print(pars.strip(tags), end='\n\n')
    
    