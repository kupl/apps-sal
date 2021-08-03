t = int(input())
for i in range(0, t):
    x, y = map(int, input().split())
    c = x % y
    print(c)
