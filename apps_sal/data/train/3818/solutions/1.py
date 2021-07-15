def get_mixed_num(f):
    [a, b] = map(int, f.split('/'))
    return "{} {}/{}".format(a//b, a%b, b)
