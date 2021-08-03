def encrypt(s):
    n = len(s[1:-1])
    while n > 9:
        n = sum(map(int, str(n)))
    return f'{s[0]}{n}{s[-1]}'


def same_encryption(s1, s2):
    return encrypt(s1) == encrypt(s2)
