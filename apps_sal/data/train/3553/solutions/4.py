import re


def show_me(s):
    return bool(re.match('[A-Z][a-z]*(-[A-Z][a-z]*)*$', s))
