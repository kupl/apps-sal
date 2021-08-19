n = int(input())
for i in range(n):
    (a, b) = list(map(int, input().split()))
    if a > b:
        t = a // b
        max1 = 1
        ans = 0
        while t >= t / 2:
            ans = (a - b * t) * t
            max1 = max(ans, max1)
            t -= 1
        print(max1)
    else:
        print(0)
