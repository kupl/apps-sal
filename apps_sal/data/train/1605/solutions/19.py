a, b = list(map(int, input().split(' ')))
res = a * (a * b + b + 2) * (b - 1) * b // 4
md = 10**9 + 7
print(res % md)
