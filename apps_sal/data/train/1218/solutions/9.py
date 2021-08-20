tc = int(input())
for i in range(0, tc):
    (x, n) = map(int, input().split())
    i = 1
    asum = 0
    while x * i < n:
        asum = asum + x * i
        i += 1
    print(asum)
