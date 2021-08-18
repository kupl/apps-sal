t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    right = l
    lmin = l[0]
    left = l
    rmin = l[n - 1]
    for i in range(0, n):
        left[i] = min(lmin, l[i])
        lmin = left[i] + 1
    i = n - 1
    while i >= 0:
        right[i] = min(rmin, l[i])
        rmin = right[i] + 1
        i -= 1
    s = ""
    for i in range(n):
        s += str(min(left[i], right[i])) + " "
    print(s.strip())
