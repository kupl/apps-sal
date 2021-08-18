
def hcf(x, y):
    if x > y:
        s = y
    else:
        s = x
    for i in range(1, s + 1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf


T = int(input())
for i in range(T):
    n, m = list(map(int, input().split()))
    h = hcf(n, m)
    l = m * n
    print(l // h)
