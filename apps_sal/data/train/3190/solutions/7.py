def solve(a, b):
    a1 = (a + 99) // 100 * 100
    b1 = b // 100 * 100
    print((a1, b1))
    if a1 > b1:
        return sum((isok(x) for x in range(a, b)))
    n = sum((isok(x) for x in range(a, a1))) + sum((isok(x) for x in range(b1, b)))
    for k in range(a1, b1, 100):
        if str(k)[:2] in p2:
            for i in (0, 1, 25, 76):
                if str((k + i) ** 2)[:2] in p2:
                    n += 1
    return n


def isok(n):
    return n % 100 in (0, 1, 25, 76) and str(n)[:2] in p2 and (str(n * n)[:2] in p2)


p2 = ('11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97')
