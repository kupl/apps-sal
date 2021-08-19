import bisect
X = int(input())
K = int(input())
R = list(map(int, input().split()))
R.append(0)

A = [X for _ in range(K + 1)]
B = [0 for _ in range(K + 1)]
C = [X for _ in range(K + 1)]
D = [0 for _ in range(K + 1)]
state = -1
for i in range(K):
    dr = R[i] - R[i - 1]
    if state == -1:
        C[i + 1] = max(0, C[i] - dr)
        D[i + 1] = max(0, D[i] - dr)
        B[i + 1] = min(B[i] + (-min(0, D[i] - dr)), A[i])
        A[i + 1] = A[i]

    else:
        C[i + 1] = min(X, C[i] + dr)
        D[i + 1] = min(X, D[i] + dr)
        A[i + 1] = max(A[i] - max(0, C[i] + dr - X), B[i])
        B[i + 1] = B[i]

    state *= -1
"""
print(A)
print(B)
print(C)
print(D)
"""

Q = int(input())
R.pop()
for _ in range(Q):
    t, a = list(map(int, input().split()))
    j = bisect.bisect_right(R, t)
    if j == 0:
        r = 0
    else:
        r = R[j - 1]
    pre_ans = (min(A[j], max(B[j], a)) - B[j]) + D[j]
    # print(pre_ans)
    pre_ans += ((-1)**(1 - j % 2)) * (t - r)
    #print(j, t, r)
    print((min(X, max(0, pre_ans))))
