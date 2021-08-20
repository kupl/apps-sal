plumm = '8WTYUIOAHXVM'


def owl_pic(text):
    wing = [c for c in text.upper() if c in plumm]
    return ''.join(wing) + "''0v0''" + ''.join(reversed(wing))
