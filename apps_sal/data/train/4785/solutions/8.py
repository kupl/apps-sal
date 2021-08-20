import requests
from bs4 import BeautifulSoup
import re


def get_member_since(username):
    soup = BeautifulSoup(requests.get('https://www.codewars.com/users/' + username).text, 'html.parser')
    return str(re.findall('Member Since:</b>........</div>?', str(soup.body.div.div.main.section)))[19:27]
