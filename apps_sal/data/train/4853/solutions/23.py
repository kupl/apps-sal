def double_char(s):
    return ''.join(map(lambda x:''.join(x), zip(s,s)))
