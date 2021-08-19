def owl_pic(text):
    plumage = ''.join((c for c in text.upper() if c in '8WTYUIOAHXVM'))
    return f"{plumage}''0v0''{plumage[::-1]}"
