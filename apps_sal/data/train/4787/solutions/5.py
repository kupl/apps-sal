def remove(s):
    count = s.count('!')
    return s.replace('!', '') + '!' * count
