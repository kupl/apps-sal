(n, q, k) = map(int, input().split())
a = [int(x) for x in input().split()]
s = input()
m = 0
l = 0
for i in a:
    if i == 1:
        m += 1
    else:
        m = 0
    if m >= k:
        l = k
        break
    elif m > l:
        l = m
for i in s:
    if i == '?':
        print(l)
    else:
        a.insert(0, a[n - 1])
        a.pop()
        if a[0] != 0:
            m = 0
            l = 0
            for j in a:
                if j == 1:
                    m += 1
                else:
                    m = 0
                if m >= k:
                    l = k
                    break
                elif m > l:
                    l = m
