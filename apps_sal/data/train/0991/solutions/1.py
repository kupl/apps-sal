mod = 10**9 + 7
N, K, Q = list(map(int, input().split()))

A = [0, 0]
# min_t=[-1]*((N*N-1)/2)
# print min_t
a, b, c, d, e, f, r, s, t, m, A[1] = list(map(int, input().split()))

L1, La, Lc, Lm, D1, Da, Dc, Dm = list(map(int, input().split()))

tmpt = t
min_arr = [0]
for x in range(2, N + 1):
    tmpt = (tmpt * t) % s
    if tmpt <= r:
        A.append((A[x - 1] * (a * A[x - 1] + b) + c) % m)
    else:
        A.append((A[x - 1] * (d * A[x - 1] + e) + f) % m)
for x in range(1, N - K + 2):
    min_arr.append(min(A[x:x + K]))

res_sum = 0
res_pro = 1
for x in range(1, Q + 1):
    L1 = (La * L1 + Lc) % Lm
    D1 = (Da * D1 + Dc) % Dm
    L = L1 + 1
    R = min(L + K - 1 + D1, N)
    R = R - K + 1
    # print min_arr,L,R,min_arr[L:R+1]
    if L == R:
        tmp = min_arr[L]
    else:
        tmp = min(min_arr[L:R + 1])
    res_sum += tmp
    res_pro = (res_pro * tmp) % mod
print(res_sum, res_pro)
