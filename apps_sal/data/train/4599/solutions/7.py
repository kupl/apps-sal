def owl_pic(text):
    wing = ''.join((c for c in text.upper() if c in '8WTYUIOAHXVM'))
    return ''.join((wing, "''0v0''", wing[::-1]))
