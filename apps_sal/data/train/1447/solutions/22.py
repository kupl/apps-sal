for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    u = []
    t = []
    ut = []
    qw = []
    c = 0
    for i in l:
        if i not in u:
            u.append(i)
            t.append(l.count(i))
    for i in t:
        if i not in ut:
            ut.append(i)
    for i in l:
        if i not in qw or qw[-1] == i:
            qw.append(i)
        else:
            print("NO")
            c = 1
            break
    if c == 0 and len(ut) == len(t):
        print("YES")
    elif c == 0:
        print("NO")
