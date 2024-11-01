from parser.parser import BaseParser, HTMLParser
from JSONGenerator.JSONDataGenerator import JSONDataGenerator
import asyncio
from bs4 import BeautifulSoup # type: ignore


pars = HTMLParser(url='https://quotes.toscrape.com')



async def generate_data(page: int):
    page_to_parse = [f'/page/{i}/' for i in range(1, page + 1)]
    tasks = [pars.fetch(page) for page in page_to_parse]
    
    fetch_res = await asyncio.gather(*tasks)
    
    json_gen = JSONDataGenerator()
    
    for data in fetch_res:
        pars_data = pars.get_data(data, 'div', 'quote')
        for e in pars_data:
            author = pars.get_data(e, 'small', 'author')
            quote = pars.get_data(e, 'span', 'text')
            tags = pars.get_data(e, 'a', 'tag')
            
            for element in json_gen.json:
                if pars.strip(author) in element.values():
                    element['quotes'].append({
                        'quote': pars.strip(quote),
                        'tags': pars.strip(tags)
                    })              
                    break
            else:
                a_tags = pars.get_data(e, 'a')
                    
                author_data = await pars.fetch(pars._get_href(a_tags[0]))
                author_born_date = pars.get_data(author_data, 'span', 'author-born-date')
                author_born_location = pars.get_data(author_data, 'span', 'author-born-location')
                author_description = pars.get_data(author_data, 'div', 'author-description')
                   
                json_gen.add_item({
                    'author': pars.strip(author),
                    'authorBornDate': pars.strip(author_born_date), 
                    'authorBornLocation': pars.strip(author_born_location),
                    'authorDescription ': pars.strip(author_description),
                    'quotes': [{'quote': pars.strip(quote),
                            'tags': pars.strip(tags)
                            }],
                })
                    
                    
    json_gen.save_to_file('quotes.json')   
    
if __name__ == '__main__':
    asyncio.run(generate_data(12))

