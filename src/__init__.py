from bs4 import *
import requests
import helper


def main(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.findAll(name='img')
    helper.create_folder(images)


input_url = input("Enter URL: ")
main(input_url)
