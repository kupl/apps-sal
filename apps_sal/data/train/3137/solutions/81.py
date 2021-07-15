from math import ceil, floor

def round_it(n):
    s = str(n).split('.')
    n_pre = len(s[0])
    n_post = len(s[1])
    print(n_pre)
    print(n_post)
    if n_pre < n_post:
        return ceil(n)
    elif n_pre > n_post:
        return floor(n)
    else:
        return round(n)
