for _ in range(int(input())):
    n = int(input())
    l = []
    for i in range(n):
        s = input()
        a = list(s)
        l = l + a
    m = ['o', 'd', 'h', 'f']
    n = []
    x = l.count('c')
    n.append(x // 2)
    y = l.count('e')
    n.append(y // 2)
    for j in range(4):
        a = l.count(m[j])
        n.append(a)
    print(min(n))
