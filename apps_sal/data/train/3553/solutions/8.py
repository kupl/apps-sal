import re


def show_me(name):
    return re.fullmatch('[A-Z][a-z]*(-[A-Z][a-z]*)*', name) is not None
