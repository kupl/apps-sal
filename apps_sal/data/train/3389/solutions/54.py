import regex as re

def domain_name(url):
    return re.sub('(https?:\/\/|www\.)*([^.]*)\..*', r'\2', url)
