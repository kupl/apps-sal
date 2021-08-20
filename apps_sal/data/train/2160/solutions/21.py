3
'\nn, k = map(int, input().split())\ndays = list(map(int, input().split()))\n\nnb_bags=0\ncrt_cap=0\nfor i in range(n):\n\tif crt_cap !=0:\n\t\tdays[i] = max(days[i]-(k-crt_cap), 0)\n\t\tcrt_cap = 0\n\t\tnb_bags += 1\n\tnb_bags += int(days[i]/k)\n\tcrt_cap = days[i]%k\n\nif crt_cap !=0:\n\tnb_bags += 1\n\nprint(nb_bags)\n'
(n, k) = map(int, input().split())
d = list(map(int, input().split()))
total = sum(d)
tab = []
tab2 = []
som = 0
nbV = 0
for d0 in d:
    som += d0
    nbV += 1
    tab.append(som)
    tab2.append(nbV)
answer_list = []
if total % k != 0:
    print('No')
else:
    d_unit = total // k
    u0 = d_unit
    v_cpt = 0
    while u0 <= total:
        if u0 > total:
            break
        if not u0 in tab:
            break
        ind = tab.index(u0)
        answer_list.append(tab2[ind] - v_cpt)
        v_cpt = tab2[ind]
        u0 += d_unit
    if u0 > total:
        print('Yes')
        print(*answer_list, sep=' ')
    else:
        print('No')
