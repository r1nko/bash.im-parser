import urllib.request
import sys
from bs4 import BeautifulSoup

output = open('bashim.txt', 'w')

def get_html(url):
	response = urllib.request.Request(
    url, 
    data=None, 
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
	)
	f = urllib.request.urlopen(response)
	return f.read()

def parse(html):
	soup = BeautifulSoup(html)
	body = soup.find_all('div', class_='text')
	for quote in body:
		output.write(str(quote.text))
		output.write('\n')


def main():
	parse (get_html('http://bash.im/'))

if __name__ == '__main__':
	main()

