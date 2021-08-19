def smash(words):
    t = ''
    for x in words:
        t = t + ''.join(x)
        if x != words[-1]:
            t += ' '
    return t
