def longer(s):
    words = s.split(' ')
    return ' '.join(sorted(words, key = lambda x: (len(x),x)))
