def smash(words):
    c = ''
    for i in words:
        c = c + ' ' + ''.join(i)
    return c.lstrip()
