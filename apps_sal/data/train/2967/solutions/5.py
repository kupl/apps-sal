def from_base(string, base, alphabet='0123456789abcdef'):
    return sum(alphabet.index(c) * base ** i for i, c in enumerate(string.lower()[::-1]))


def to_base(n, base, alphabet='0123456789abcdef'):
    s = ''
    while n:
        n, m = divmod(n, base)
        s = alphabet[m] + s
    return s or alphabet[0]


def bin_to_hex(string):
    return to_base(from_base(string, 2), 16)


def hex_to_bin(string):
    return to_base(from_base(string, 16), 2)
