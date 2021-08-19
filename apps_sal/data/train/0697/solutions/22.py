# cook your dish here
for u in range(int(input())):
    n, k = list(map(int, input().split()))
    l = list(map(int, input().split()))
    s = 0
    d = [0]
    for i in l:
        s += i
        d.append(s)
    m = 0
    for i in range(k, n + 1):
        r = d[i] - d[i - k]
        m = max(m, r)
    print(m)
