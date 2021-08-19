def dbl_linear(n):
    (u, i, c) = ({1}, 0, 1)
    while i < n:
        if c / 2 in u or c / 3 in u:
            u.add(c + 1)
            i += 1
        c += 1
    else:
        return c
