import re


def true_binary(n):
    s = bin(n)[2:]
    s = re.sub('0+1', lambda x: '1' + '0' * (len(x[0]) - 1), s)
    return [1 if c == '1' else -1 for c in s]
