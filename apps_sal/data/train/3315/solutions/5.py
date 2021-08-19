def strongest_even(n, m):
    (x, y) = (bin(n)[2:], bin(m)[2:])
    if len(x) < len(y):
        return 1 << len(y) - 1
    i = next((i for i in range(len(x)) if x[i] != y[i]))
    res = x[:i] + ('1' if '1' in x[i:] else '0') + '0' * (len(x) - i - 1)
    return int(res, 2)
