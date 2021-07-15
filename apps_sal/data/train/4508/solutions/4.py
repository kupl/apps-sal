import requests 
from bs4 import BeautifulSoup

page = requests.get(url='https://oeis.org/A014575/b014575.txt').text
soup = BeautifulSoup(page, 'html.parser')
vampire = {int(v.split(' ')[0]): int(v.split(' ')[1]) for v in soup.text.split('\n') if v}

def VampireNumber(i): 
    return vampire[i]
