def encode(s):
    first_to_last = lambda x: x[1:] + x[0]
    return ' '.join((first_to_last(x[::-1]) for x in s.split()))
