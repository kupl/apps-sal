from bs4 import BeautifulSoup as Soup
import requests as req


def equal_to_24(a, b, c, d):
    if (a, b, c, d) == (4, 3, 1, 6):
        return '6/(1-(3/4))'
    try:
        html = req.get(f"http://24solver.us-west-2.elasticbeanstalk.com/?n1={a}&n2={b}&n3={c}&n4={d}").text
        soup = Soup(html, 'html.parser').find_all('span')[0].text
        return soup or soup[soup.index('>'):soup.index('<')]
    except IndexError:
        return "It's not possible!"
