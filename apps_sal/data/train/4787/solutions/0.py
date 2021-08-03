def remove(s):
    return s.replace('!', '') + s.count('!') * '!'
