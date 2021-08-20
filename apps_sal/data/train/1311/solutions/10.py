for t in range(int(input())):
    (n, k) = list(map(int, input().split()))
    flips = n - k
    A = []
    for i in range(n):
        a = i
        if (i + 1) % 2 == 0 and flips > 0:
            A.append(-(a + 1))
            flips -= 1
        else:
            A.append(a + 1)
    if flips > 0:
        if n % 2:
            last_odd = n - 1
        else:
            last_odd = n - 2
        while flips > 0:
            A[last_odd] *= -1
            flips -= 1
            last_odd -= 2
    print(*A)
