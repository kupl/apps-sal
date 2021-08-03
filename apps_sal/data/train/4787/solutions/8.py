def remove(s):
    c = s.count('!')
    s = s.replace('!', '')
    return s + '!' * c
