try:
    for a in range(1, int(input()) + 1):
        L, K = input().split()
        L, K = int(L), int(K)
        if L < K:
            c = 0
        else:
            c = L - K + 1
        s = (c * (c + 1)) // 2
        print("Case", str(a) + ":", s)
except:
    pass
