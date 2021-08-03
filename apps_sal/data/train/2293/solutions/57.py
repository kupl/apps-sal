N = int(input())
A = list(map(int, input().split()))
M = 2 ** N

ans = [0] * M
max_list = [0] * M
for i in range(1, M):
    cand = [i]
    ans_cand = []
    ibin = bin(i)[2:].zfill(N)
    for j in range(N):
        if ibin[j] == '1':
            cand.append(max_list[i - 2 ** (N - j - 1)])
            ans_cand.append(ans[i - 2 ** (N - j - 1)])
    cand_set = sorted(list(set(cand)))
    max1 = 0
    max2 = 0
    for c in cand_set:
        Ac = A[c]
        if Ac >= max1:
            max2 = max1
            max1 = Ac
            max_idx = c
        elif Ac > max2:
            max2 = Ac
    ans_cand.append(max1 + max2)
    ans_cand.append(ans[i - 1])
    max_list[i] = max_idx
    ans[i] = max(ans_cand)
    print((ans[i]))
