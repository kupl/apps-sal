from urllib.request import urlopen
from bs4 import BeautifulSoup as bs


def get_member_since(username):
    html = urlopen(f'https://www.codewars.com/users/{username}')
    soup = bs(html.read(), 'html.parser')
    tags = soup.find_all('div', {'class': 'stat'})
    member_tag = [x.text for x in tags if 'Member Since' in x.text][0]
    return member_tag.split(':')[1]
