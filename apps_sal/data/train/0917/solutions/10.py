for i in range(int(input())):
    (n, k) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    ind = 1
    m = 10 ** 10
    for i in range(n):
        for j in range(i + 1, n):
            if abs(m) > abs(a[i] + a[j] - k):
                m = abs(a[i] + a[j] - k)
                ind = 1
            elif abs(m) == abs(a[i] + a[j] - k):
                ind += 1
    print(m, ind)
