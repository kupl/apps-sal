for _ in range(int(input())):
    l = []
    lll = []
    s = 0
    n = int(input())
    for _ in range(n):
        ll = list(map(str, input().split()))
        s += int(ll[2])
        lll.append(ll)
    avg = s // n
    for i in lll:
        if int(i[2]) < avg:
            l.append(i)
    l.sort(key=lambda x: x[2])
    for i in l:
        print(*i)
