3

'''
n, k = map(int, input().split())
days = list(map(int, input().split()))

nb_bags=0
crt_cap=0
for i in range(n):
	if crt_cap !=0:
		days[i] = max(days[i]-(k-crt_cap), 0)
		crt_cap = 0
		nb_bags += 1
	nb_bags += int(days[i]/k)
	crt_cap = days[i]%k

if crt_cap !=0:
	nb_bags += 1

print(nb_bags)
'''


n, k = map(int, input().split())
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
    print("No")
else:
    d_unit = total // k
    u0 = d_unit
    v_cpt = 0
    while u0 <= total:
        if u0 > total:
            break
        if not(u0 in tab):
            break
        ind = tab.index(u0)
        answer_list.append(tab2[ind] - v_cpt)
        v_cpt = tab2[ind]
        u0 += d_unit
    if u0 > total:
        print("Yes")
        print(*answer_list, sep=' ')
    else:
        print("No")
