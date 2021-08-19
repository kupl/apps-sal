T = int(input())
for a in range(T):
    Q = int(input())
    l2 = []
    even = 0
    odd = 0
    for _ in range(Q):
        l3 = []
        z = int(input())
        if z not in l2:
            x = str(bin(z))
            if x.count('1') % 2 == 0:
                even += 1
            else:
                odd += 1
            for w in l2:
                l3.append(w ^ z)
                x = str(bin(w ^ z))
                if x.count('1') % 2 == 0:
                    even += 1
                else:
                    odd += 1
            l2.append(z)
            l2.extend(l3)
        print(even, end=' ')
        print(odd)
