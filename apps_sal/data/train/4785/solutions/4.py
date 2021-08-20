from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_member_since(username):
    return BeautifulSoup(urlopen(f'https://www.codewars.com/users/{username}')).find(text='Member Since:').next_element
