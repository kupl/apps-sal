def encode(s):
    return ''.join(((x, str(~ord(x) % 2))[x.isalpha()] for x in s))
