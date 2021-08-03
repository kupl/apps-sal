m, n, a = 1000000007, int(input()), input().split()
print(pow(2, n - 1, m) - 1 - sum(pow(2, a.count(x), m) - 1 for x in set(a) if x != '-1') % m)
