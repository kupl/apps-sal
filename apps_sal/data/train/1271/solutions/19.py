T = int(input())
for a in range(T):
    Q = int(input())
    l2 = []
    for _ in range(Q):
        even = 0
        odd = 0
        l3 = []
        z = int(input())
        if z not in l2:
            for w in l2:
                l3.append(w ^ z)
            l3.append(z)
            l2.extend(l3)
        for q in l2:
            x = str(bin(q))
            if x.count('1') % 2 == 0:
                even += 1
            else:
                odd += 1
        print(even, end=' ')
        print(odd)
