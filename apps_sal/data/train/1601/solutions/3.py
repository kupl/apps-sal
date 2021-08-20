t = int(input())
while t:
    (n, p) = map(int, input().split())
    if n <= 2:
        print(p * p * p)
    else:
        max = int((n - 1) / 2)
        c = (p - max) * (p - max)
        c = c + (p - n) * (p - max)
        c = c + (p - n) * (p - n)
        print(c)
    t = t - 1
