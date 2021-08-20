t = int(input())
while t > 0:
    (b, g) = input().split()
    b = int(b)
    g = int(g)
    ans = (abs(b + g) - 1) * 2
    print(ans)
    t = t - 1
