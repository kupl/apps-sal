from re import sub


def hex_hash(code):
    return sum(sum(map(int, sub("[^0-9]", "", hex(ord(c))))) for c in code)
