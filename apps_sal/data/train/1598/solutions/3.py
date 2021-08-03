# cook your dish here
for _ in range(int(input())):
    l = []
    lll = []
    s = 0
    n = int(input())
    for _ in range(n):
        ll = list(map(str, input().split()))
        s += float(ll[2])
        lll.append(ll)
    avg = s / n
    # print(avg)
    for i in lll:
        if float(i[2]) < avg:
            l.append(i)
    # print(l,lll)
    l.sort(key=lambda x: x[2])
    for i in l:
        print(*i)
