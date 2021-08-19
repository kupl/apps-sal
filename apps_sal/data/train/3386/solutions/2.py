alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def get_column_title(n):
    if n < 1:
        raise ValueError
    l = []
    while n:
        (n, m) = divmod(n - 1, 26)
        l.append(alpha[m])
    return ''.join(l[::-1])
