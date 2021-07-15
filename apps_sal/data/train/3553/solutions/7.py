import re

def show_me(name):
    return re.match( '^[A-Z][a-z]*(-[A-Z][a-z]*)*$', name) != None
