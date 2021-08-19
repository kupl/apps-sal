import re


def has_subpattern(string):
    # print(string)
    n = len(string)
    if n == 1:
        return False
    l, h = '{}'
    for i in range(1, n):
        # print(f'({string[:i]}){l}{n/i}{h}')
        if n % i == 0 and string[:i] * (n // i) == string:
            # print(string[:i])
            return True
    return False
