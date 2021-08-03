# cook your dish here
t = int(input())
while t > 0:
    n, k, l = map(int, input().split())
    l1 = []
    if k * l < n:
        print("-1")
    elif n > 1 and k == 1:
        print("-1")
    else:
        o = 1
        for i in range(n):
            l1.append(o)
            o += 1
            if o > k:
                o = 1
        print(*l1)
    t -= 1
