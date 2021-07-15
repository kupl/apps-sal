def make_upper_case(s):
    return "".join([chr(ord(n) - 32) if ord(n) >= 97 else n for n in s])
