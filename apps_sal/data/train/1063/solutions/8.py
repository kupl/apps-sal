n = int(input())
while n > 0:
    x, y = map(int, input().strip().split())
    print(x % y)
    n = n - 1
