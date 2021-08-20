alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
vo = ['a', 'e', 'i', 'o', 'u']
con = []
for i in alp:
    if i not in vo:
        con.append(i)
for _ in range(int(input())):
    sm = 0
    uin = input().strip()
    for i in uin:
        if i in vo:
            continue
        else:
            mn = 100
            for j in vo:
                if abs(alp.index(i) + 1 - (alp.index(j) + 1)) < mn:
                    mn = abs(alp.index(i) + 1 - (alp.index(j) + 1))
            sm = sm + mn
    print(sm)
