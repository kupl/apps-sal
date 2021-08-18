def hcf(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


l = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    r = int(input())
    s = a[0]
    for i in range(1, n):
        s = (s * a[i]) // hcf(s, a[i])
    l.append(s + r)
for i in l:
    print(i)
