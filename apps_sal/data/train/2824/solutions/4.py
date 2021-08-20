def encode(s):
    return ' '.join([i[:-1][::-1] + i[-1] for i in s.split(' ')])
