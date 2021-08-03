N = int(input())
NN = (1 << N)
A = list(map(int, input().split()))
dp1 = A[:]
dp2 = [0] * (NN)
for k in range(N):
    bit = 1 << k
    for i in range(NN):
        if not i & bit:
            if dp1[i] > dp1[i | bit]:
                dp2[i | bit] = max(dp1[i | bit], dp2[i])
                dp1[i | bit] = dp1[i]
            elif dp1[i] > dp2[i | bit]:
                dp2[i | bit] = dp1[i]
res = 0
for a, b in zip(dp1[1:], dp2[1:]):
    res = max(res, a + b)
    print(res)
