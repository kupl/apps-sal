import re
PLUMAGE = re.compile('[8WTYUIOAHXVM]')


def owl_pic(text):
    left = ''.join(PLUMAGE.findall(text.upper()))
    return f"{left}''0v0''{left[::-1]}"
