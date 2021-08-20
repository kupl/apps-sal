from collections import Counter
for _ in range(int(input())):
    n = int(input())
    l = [i for i in input().split()]
    ll = []
    c = Counter(l)
    cc = []
    m = 0
    for (l, count) in c.most_common(len(l) - 1):
        if m == 0:
            ll.append(l)
            cc.append(count)
        if m == count:
            ll.append(l)
            cc.append(count)
        if count < m:
            break
        m = count
    k = set(cc)
    leng = len(list(k))
    if leng == 1:
        sor = sorted(ll)
        print(sor[0])
    else:
        print(ll[0])
