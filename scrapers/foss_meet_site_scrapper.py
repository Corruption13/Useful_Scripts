# Script to check FOSSMEET website status (Don't ask why)
import requests
from bs4 import BeautifulSoup
import time

def request_url(url):
    r=requests.get(url)
    return r.text
def check_html():
    if "Registrations aren't open yet. Please check back later" not in request_url("https://www.fossmeet.in/"):
        print("alret")
    else:
        print("no alert")

if __name__=='__main__':
    i=1
    while(True):
        print(f"{i} run: ",end="")
        check_html()
        i+=1
        time.sleep(10)
