n = int(input())
print('YES')
for _ in range(n):
    x, y, *z = list(map(int, input().split()))
    print((x & 1) * 2 + (y & 1) + 1)
