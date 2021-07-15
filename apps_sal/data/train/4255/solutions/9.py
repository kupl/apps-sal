def make_upper_case(s):
    return ''.join(chr(ord(ch) - 32) if ord(ch) in range(97, 123) else ch for ch in s)
