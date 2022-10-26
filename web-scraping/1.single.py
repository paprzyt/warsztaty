import requests
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup 

url = "https://www.scrapethissite.com/pages/simple/"

def main():
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "lxml")

if __name__ == "__main__":
    main()
