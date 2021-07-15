def owl_pic(text):
    t = text.upper()
    r = [i for i in t if i in '8WTYUIOAHXVM']
    return ''.join(r) + "''0v0''" + ''.join(r[::-1])
