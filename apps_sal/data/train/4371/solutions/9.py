def digits(num):
    parse = lambda s: [int(s[0]) + int(x) for x in s[1:]] + (digits(s[1:]) if len(s) > 2 else [])
    return parse(str(num))

