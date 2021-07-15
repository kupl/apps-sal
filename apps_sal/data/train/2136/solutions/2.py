n = int(input())
a = list(map(int, input().split()))

ans = 0
black = 0
white = 0
for i in range(n):
    if i % 2 == 0:
        black += a[i] // 2
        white += a[i] - a[i] // 2
    elif i % 2 == 1:
        white += a[i] // 2
        black += a[i] - a[i] // 2

print(min(white, black))
