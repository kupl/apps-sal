def string_transformer(s):
    return ' '.join([i.swapcase() for i in s.split(' ')][::-1])

