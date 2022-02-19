class ProductExtractor(object):
	BASE_URL = 'http://books.toscrape.com'


import requests
def make_request(self, url):
	return requests.get(url)


from urllib.parse import urljoin
from bs4 import BeautifulSoup
def extract_urls(self, start_url):
    response = self.make_request(start_url)
    parser = BeautifulSoup(response.text, 'html.parser')
    product_links = parser.select('article.product_pod > h3 > a')
    for link in product_links:
    	relative_url = link.attrs.get('href')
    	absolute_url = urljoin(self.BASE_URL, relative_url.replace('../../..', 'catalogue'))
    yield absolute_url


def extract_product(self, url):
	    	response = self.make_request(url)
	    	parser = BeautifulSoup(response.text, 'html.parser')
	    	book_title = parser.select_one('div.product_main > h1').text
	    	price_text = parser.select_one('p.price_color').text
	    	stock_info = parser.select_one('p.availability').text.strip()
	    	product_data = {
    		'title': book_title,
    		'price': self.clean_price(price_text),
    		'stock': stock_info
	    	}
	    	return product_data
