# cook your dish her
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))

    def ki(v, n, k):
        if n < k:
            print(0)
        su = 0
        a = 0
        e = k - 1
        for i in range(k):
            su += v[i]

        for i in range(k, n + k):
            su += v[i % n] - v[(i - k) % n]
            if su > a:
                a = su

        print(a)

    ki(l, n, k)
