def remove(s):
    t = s.translate(None, '!')
    return t + '!' * (len(s) - len(t))
