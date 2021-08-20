def encode(s):
    return ' '.join((x[-2::-1] + x[-1] for x in s.split()))
