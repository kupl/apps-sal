nq = [x for x in list(map(int, input().split(' ')))]
tab = [x for x in list(map(int, input().split(' ')))]
xs = tab[0]
sol = []
sol.append(tab[0])
for i in range(1, nq[0]):
    xs ^= tab[i]
    sol.append(xs)
sol.append(sol[-1] ^ xs)
for i in range(nq[1]):
    q = int(input())
    print(sol[(q - 1) % (nq[0] + 1)])
