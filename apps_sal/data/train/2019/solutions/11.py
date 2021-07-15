n, a = int(input()), [int(x) for x in input().split()]
print(max(max(a), (sum(a) + n - 2) // (n - 1)))
