# cook your dish here
for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m = 0
    for i in range(n):
        if i % 2 == 0:
            if m < 0:
                m -= a[i]
            else:
                m += a[i]
        else:
            if m < 0:
                m += a[i]
            else:
                m -= a[i]
    if abs(m) >= k:
        print(1)
    else:
        print(2)
