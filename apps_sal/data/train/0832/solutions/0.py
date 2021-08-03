def fact(n):
    if n < 2:
        return 1
    return n * fact(n - 1)


def ncr(n, r):
    return fact(n) // (fact(r) * fact(n - r))


t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    count_z = a.count(a[k - 1])
    count_z_seq = a[:k].count(a[k - 1])

    print(ncr(count_z, count_z_seq))
