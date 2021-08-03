T = int(input())
chef = []
while (T > 0):
    T -= 1
    NM = input().split()
    N = int(NM[0])
    M = int(NM[1])

    soints = dict()
    sofloats = dict()

    for i in range(0, N):
        CL = input().split()
        C = int(CL[0])
        L = int(CL[1])
        if L in soints:
            soints[L] += C
        else:
            soints[L] = C

    for i in range(0, M):
        CL = input().split()
        C = int(CL[0])
        L = int(CL[1])
        if L in sofloats:
            sofloats[L] += C
        else:
            sofloats[L] = C

    chef_val = 0
    for i in soints:
        if sofloats[i] - soints[i] > 0:
            chef_val += sofloats[i] - soints[i]

    chef.append(chef_val)
for i in chef:
    print(i)
