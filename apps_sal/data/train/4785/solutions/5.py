from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_member_since(username):
    page = urlopen('https://www.codewars.com/users/' + username)
    soup = BeautifulSoup(page, 'html.parser')

    for i in soup.select('.stat'):
        if ("Member Since" in i.text.strip()):
            text = i.text.strip()
            final = text[13:]
            return final
