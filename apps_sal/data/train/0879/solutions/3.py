t = int(input())
for _ in range(t):
    (x, y) = list(map(int, input().split()))
    sum = 0
    y1 = y
    while y1 <= x:
        sum += y1 % 10
        y1 += y
    print(sum)
