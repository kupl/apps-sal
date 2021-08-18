n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    a = x if x == y else x + y
    print(max(x, y), a)
