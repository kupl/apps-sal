import re

def digit_all (x):
    return re.sub("\D", "", x) if type(x) is str else 'Invalid input !'
