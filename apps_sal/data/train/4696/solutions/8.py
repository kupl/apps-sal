def same_encryption(a, b):

    def f(s):
        return f'{s[0]}{(len(s) - 2) % 9 or 9}{s[-1]}'
    return f(a) == f(b)
