def check2(r, x, k, j):
    if k % r == 0 and j % r == 0:
        return True
    if k % x == 0 and j % x == 0:
        return True
    return False


def check(r, c, m, k, j):
    if m % r != 0:
        return False
    x = c - m / r
    return check2(r, x, k, j)


for _ in range(int(input())):
    (r, c, m, k, j) = list(map(int, input().split()))
    if r * c != m + k + j:
        print('No')
    else:
        b = False
        b |= check(r, c, m, k, j)
        b |= check(r, c, k, m, j)
        b |= check(r, c, j, m, k)
        b |= check(c, r, m, k, j)
        b |= check(c, r, k, m, j)
        b |= check(c, r, j, m, k)
        if b:
            print('Yes')
        else:
            print('No')
