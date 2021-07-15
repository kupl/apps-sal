def super_size(n):
    if n < 0:
        raise ValueError
    elif n < 10:
        return n
    else:
        ans = sorted(str(n), reverse=True)
        return int("".join(ans))
