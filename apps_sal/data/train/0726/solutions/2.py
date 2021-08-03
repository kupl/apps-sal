t = int(input())
for i in range(t):
    n = int(input())
    l = []
    for k in range(n):
        s = input()
        l.append(s)
    s = ''.join(l)
    f = "odhf"
    m = []
    for j in f:
        m.append(s.count(j))
    m.append(s.count('c') // 2)
    m.append(s.count('e') // 2)
    print(min(m))
