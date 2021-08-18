n = int(input())
while n > 0:
    a, b = map(int, input().strip().split())
    print(max(a, b), a + b)
    n = n - 1
