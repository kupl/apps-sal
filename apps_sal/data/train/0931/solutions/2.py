for i in range(int(input())):
    m = []
    n = []
    o = []
    (s, x) = (0, 0)
    q = 0
    n = int(input())
    l = list(map(int, input().split()))
    for i in l:
        m.append(str(bin(i)))
    for j in m:
        q = q + 1
        if j[-1] == '0':
            s = s + l[q - 1]
    o.append(s)
    for j in range(len(o)):
        print(o[j])
