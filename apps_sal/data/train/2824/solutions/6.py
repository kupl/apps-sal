def encode(s):
    k = ' '.join([i[::-1][1:] + i[::-1][0] for i in s.split(' ')])
    return k
