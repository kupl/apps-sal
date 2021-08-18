t = int(input())
while t:
    x = 0
    n = int(input())
    b = list(map(int, input().strip().split()))
    p = list(map(float, input().strip().split()))
    for i in range(30):
        pb = 0.0
        for j in range(n):
            if b[j] & (1 << i):
                pb = pb * (1 - p[j]) + (1 - pb) * p[j]
        x += (1 << i) * pb
    print(x)
    t -= 1
