try:
    M = int(input())
    BNA = list(map(int, input().split()))
    N = int(input())
    BN = []
    for i in range(N):
        BN.append(int(input()))
    l = []
    for i in BN:
        l.append(BNA[i-1])
        BNA.remove(BNA[i-1])
    print('\n'.join(map(str, l)))
except:
    pass

