t = int(input())
while t > 0:
    t -= 1
    (n, m) = input().split()
    n = int(n)
    m = int(m)
    b = [1] * (n + 1)
    c = [1] * (n + 1)
    while m > 0:
        m -= 1
        (i, j, k) = input().split()
        i = int(i)
        j = int(j)
        k = int(k)
        b[i - 1] *= k
        c[j] *= k
    ar = [10] * (n + 1)
    ar[0] = b[0]
    ar[0] /= c[0]
    for i in range(n):
        ar[i] = ar[i - 1]
        ar[i] *= b[i]
        ar[i] /= c[i]
    Sum = 0
    for i in range(n):
        Sum += ar[i]
    print(int(Sum / n))
