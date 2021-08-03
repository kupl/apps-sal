n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        t = a // b
        max1 = 1
        ans = 0
        while(t > 0):
            ans = (a - b * t) * t
            max1 = max(ans, max1)
            t -= 1
        print(max1)
    else:
        print(0)
