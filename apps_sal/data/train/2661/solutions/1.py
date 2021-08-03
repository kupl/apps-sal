import re


def find_codwars(url):
    domain = url.split('//')[-1]
    domain = domain.split('/')[0]
    domain = domain.split('?')[0]
    return domain.split('.')[-2:] == ['codwars', 'com']
