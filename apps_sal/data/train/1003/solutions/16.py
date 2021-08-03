T = int(input())

for t in range(0, T):
    N, M = input().split()

    I = []
    F = []

    for n in range(0, int(N)):
        C, L = input().split()
        I.append((int(C), int(L)))

    for n in range(0, int(M)):
        C, L = input().split()
        F.append((int(C), int(L)))

    chakra = 0

    for l in set([i[1] for i in I]):
        Cil = [i[0] for i in I if i[1] == l]
        Cfl = [f[0] for f in F if f[1] == l]
        temp = (sum(Cfl) - sum(Cil))
        if temp > 0:
            chakra += temp

    print(chakra)
