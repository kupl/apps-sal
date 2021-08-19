import re


def show_me(name):
    return bool(re.match('(-[A-Z][a-z]+)+$', '-' + name))
