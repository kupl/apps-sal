n = int(input())
a = [list(map(int, input().split())) for x in range(n)]
result = [0] * n
for x in range(1, n):
    result[max(list(range(n)), key = lambda i: a[i].count(x))] = x
print(*[(x if x else n) for x in result])

