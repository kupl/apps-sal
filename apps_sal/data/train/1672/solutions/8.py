a = 11

arr = []

while a > 0:

    n = int(input())

    arr.append(n)

    a -= 1

for el in arr[::-1]:

    q = abs(el) ** 0.5
    w = el ** 3 * 5

    e = q + w

    if e > 400:
        print('f({}) = MAGNA NIMIS!'.format(el))

    else:
        print('f({}) = {:.2f}'.format(el, e))
