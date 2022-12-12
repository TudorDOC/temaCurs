import requests
from bs4 import BeautifulSoup
import configparser

url = input("Enter an URL: ")
data = requests.get(url)  # luam codul sursa a paginii html
# Folosim un obiect SOUP ca sa putem prelucra datele in continuare
soup = BeautifulSoup(data.text, "html.parser")

#fisier configurare
def config_file():
    '''Se scrie in fisierul de configurare un url default'''
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'url': '"https://www.python.org"'}
    with open('example.ini', 'w') as configfile:
        config.write(configfile)
  
def print_title(soup):
    '''
    Functia printeaza titlul paginii, si primeste ca parametru obiectul de tip soup
    '''
    # cautam titlul paginii
    title = soup.find("title")
    print("Titlul paginii introduse este: " + title.get_text())


def print_meta_description(soup):
    '''Functia primeste ca parametrul un obiect soup, si afiseaza meta description'''
    meta = soup.find('meta', attrs={'name': 'description'})
    print("Description meta: " + meta["content"])



print_title(soup)
print_meta_description(soup)
