from itertools import takewhile

def remove_url_anchor(url):
    return ''.join(takewhile(lambda l: l != '#', url))
