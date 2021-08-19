# cook your dish here
def tourneyscore(a):
    scorelist = [0 for i in range(len(a))]
    for i in range(len(a)):
        for k in range(i + 1, len(a)):
            if a[i][0] < a[k][0]:
                if a[i][1] > a[k][1]:
                    scorelist[i] += 2
                else:
                    scorelist[i] += 1
                    scorelist[k] += 1
            else:
                if a[i][1] < a[k][1]:
                    scorelist[k] += 2
                else:
                    scorelist[i] += 1
                    scorelist[k] += 1
    print(*scorelist, sep=" ")


for T in range(int(input())):
    singerlist = []
    for N in range(int(input())):
        L, U = input().split()
        L, U = int(L), int(U)
        singerlist.append([L, U])
    tourneyscore(singerlist)
