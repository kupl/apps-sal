N, = list(map(int, input().split()))
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
mxk = 29
msk = (1<<mxk) - 1
msk2 = (1<<(mxk-1))
r = 0
for i in range(mxk):
    # 下からiビット目をみる
    for j in range(N):
        Q[j] = Q[j] & msk
        P[j] = P[j] & msk
    msk >>= 1
    P.sort()
    Q.sort()
    j1 = N-1
    j2 = N-1
    b = 0
    ss = N
#    print(P, Q)
    for l in range(N):
        if P[l] & msk2:
            ss = l
            break
        k1 = msk2 - (P[l]&msk)
        k2 = k1 + msk2
        while j1 >= 0:
            if Q[j1] < k1:
                break
            j1 -= 1
        while j2 >= 0:
            if Q[j2] < k2:
                break
            j2 -= 1
        b += j2 - j1
#        print("a",j2-j1,k1,k2,j1,j2)

    j1 = N-1
    j2 = N-1
#    print(ss)
    for l in range(ss, N):
        k1 = msk2 - (P[l]&msk)
        k2 = k1 + msk2
        while j1 >= 0:
            if Q[j1] < k1:
                break
            j1 -= 1
        while j2 >= 0:
            if Q[j2] < k2:
                break
            j2 -= 1
#        print("b",j1 - j2 + N)
        b += j1 + N - j2

#    b = 0
#    for p in P:
#        if p & msk2:
#            x = g(2*msk2 - (p&msk))
#            z = g(msk2 - (p&msk))
#            b += z+N-x
#        else:
#            x = g(2*msk2 - (p&msk))
#            z = g(msk2 - (p&msk))
#            b += x-z
#    print(b, r, i)
    if b%2:
        r += 1<<(mxk-1-i)
    msk2 >>= 1
print(r)

