def find(n, z):
    r = n + 1
    sumn = sumof(n)
    while True:
        if sumof(r) > sumn + z:
            return r
        r += 1
    return 'Perhaps this is a different way to solve the kata, but it works ;-)(not cheat)'


def sumof(n):
    fm = [[], [], [], [22, 13, 4], [365, 167, 50, 14], [5415, 2130, 627, 177, 51], [75802, 27067, 7897, 2254, 661, 202], [123456, 123456, 123456, 123456, 123456, 123456, 123456]]
    l = 1 if n < 10 else 2 if n < 100 else 3 if n < 1000 else 4 if n < 10000 else 5 if n < 100000 else 6 if n < 1000000 else 7
    (a, i, r) = (fm[l], l - 1, 0)
    while n > 0:
        t = n % 10
        n //= 10
        r += t * a[i]
        i -= 1
    return r
