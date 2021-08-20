def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = []
    for j in range(len(a) - 1):
        b.append(a[j + 1] - a[j])
    b.append(360 - a[len(a) - 1] + a[0])
    for k in range(len(b) - 1):
        b[k + 1] = hcf(b[k], b[k + 1])
    p = 360 / b[len(b) - 1]
    print(int(p - len(a)))
