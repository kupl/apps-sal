t = int(input())
for hh in range(0, t):
    (n, k) = [int(x) for x in input().split()]
    m = 1000000007
    pos = n
    if n == 0:
        rem = k - 1
        cur = rem * (rem + 1) % m
        print(cur)
    elif k == 1:
        prev = pos * (pos - 1) % m
        curr = (prev + pos) % m
        print(curr)
    elif k % 2 == 1:
        k -= 1
        p = k // 2
        ans = 2 * pos
        inipos = pos
        pos = (pos + p - 1) % m
        prev = pos * (pos + 1) % m
        now = (inipos + p) % m
        rem = (now - inipos + m) % m
        curr = (prev + now + rem) % m
        print(curr)
    else:
        k -= 1
        p = k // 2
        inipos = pos
        pos = (pos + p) % m
        prev = pos * (pos + 1) % m
        curr = (prev + inipos) % m
        print(curr)
