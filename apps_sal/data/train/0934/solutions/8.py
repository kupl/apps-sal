t = int(input())
mod = 10 ** 9 + 7
for _ in range(t):
    sum = 0
    (p, q, r) = map(int, input().split())
    a = sorted((int(x) for x in input().split()))
    b = sorted((int(x) for x in input().split()))
    c = sorted((int(x) for x in input().split()))
    t1 = t2 = sum1 = sum2 = 0
    for i in b:
        while t1 < p and a[t1] <= i:
            sum1 += a[t1]
            t1 += 1
        while t2 < r and c[t2] <= i:
            sum2 += c[t2]
            t2 += 1
        sum += (i * t1 + sum1) * (i * t2 + sum2)
    print(sum % mod)
