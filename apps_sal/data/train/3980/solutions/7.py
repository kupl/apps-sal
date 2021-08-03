from re import sub


def reverse(string):
    return sub(r'(\w)\1+', lambda m: m.group().swapcase(), string)
