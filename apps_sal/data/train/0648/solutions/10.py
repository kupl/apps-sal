(N, Q) = input().split()
N = int(N)
Q = int(Q)
L = list(input().split())
L = list(map(int, L))
while Q > 0:
    L2 = list(input().split())
    L2 = list(map(int, L2))
    le = len(L2)
    i = L2[1] - 1
    k = L2[2]
    if le == 3:
        flag = True
        while flag == True:
            jump = next((z for (z, n) in enumerate(L[i:]) if n > L[i]), len(L) + 1)
            if jump > 100 or jump == len(L) + 1:
                print(i + 1)
                flag = False
            elif k > 0:
                i = i + jump
                k = k - 1
            else:
                print(i + 1)
                flag = False
    else:
        c = L2[3]
        for i in range(i, k):
            L[i] = L[i] + c
    Q = Q - 1
