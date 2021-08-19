t = int(input())
for _ in range(t):
    (n, d) = map(int, input().split())
    c = list(map(int, input().split()))
    c.sort()
    start = 0
    end = 10 ** 12
    possible = True
    ans = None
    while start <= end:
        mid = (start + end) // 2
        current = c[0]
        for i in range(1, n):
            next = current + mid
            if next >= c[i] and next <= c[i] + d:
                current = next
                possible = True
            elif next < c[i]:
                current = c[i]
                possible = True
            else:
                possible = False
                break
        if possible:
            ans = mid
            start = mid + 1
        else:
            end = mid - 1
    start = ans
    end = ans + 1
    possible = True
    while start <= end:
        mid = (start + end) / 2
        current = c[0]
        for i in range(1, n):
            next = current + mid
            if next >= c[i] and next <= c[i] + d:
                current = next
                possible = True
            elif next < c[i]:
                current = c[i]
                possible = True
            else:
                possible = False
                break
        if possible:
            ans = mid
            start = mid + 1e-06
        else:
            end = mid - 1e-06
    print(ans - 1e-07)
