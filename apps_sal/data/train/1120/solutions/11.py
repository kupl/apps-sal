for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    (r, c) = list(map(int, input().split()))
    n -= 1
    m -= 1
    s1 = m - r + n - c
    s2 = r + c
    s3 = r + m - c
    s4 = n - r + c
    print(max(s1, s2, s3, s4))
