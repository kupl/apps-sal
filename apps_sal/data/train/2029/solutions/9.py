def most_equal(n):
    if n % 2 == 0:
        return [['NO']]
    a = list()
    for i in range(1, 2 * n + 1):
        if i <= n:
            a.append(2 * i - i % 2)
        else:
            a.append(2 * (i - n) - i % 2)
    return [['YES'], a]


m = int(input())
for elem in most_equal(m):
    print(*elem)
