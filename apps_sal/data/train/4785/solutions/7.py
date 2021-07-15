import urllib.request
import bs4
import re
def get_member_since(username):
    soup = bs4.BeautifulSoup(urllib.request.urlopen(f'https://www.codewars.com/users/{username}'))
    return re.search(r'(?<=Member Since:</b>).+?(?=</div>)',str(soup.findAll('div',attrs={'class':'stat'}))).group()
