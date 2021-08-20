def make_upper_case(s):
    return ''.join([chr(ord(x) - 32) if ord(x) in range(97, 123) else x for x in s])
