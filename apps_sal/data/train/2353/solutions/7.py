n, a = int(input()), list(map(int, input().split()))
b = sorted(a) + [min(a)]
print(' '.join([str(b[b.index(a[i]) + 1]) for i in range(n)]))
