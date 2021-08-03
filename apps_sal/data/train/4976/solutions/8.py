import re


def search(titles, term):
    return [t for t in titles if re.search(term, t, re.I)]
