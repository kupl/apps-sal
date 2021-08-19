for _ in range(int(input())):
    S = input()
    R = input()
    N = len(S)
    groups = []
    cont = False
    for i in range(N):
        if S[i] != R[i]:
            if cont:
                groups[-1][1] += 1
            else:
                groups.append([i, i])
                cont = True
        else:
            cont = False
    k = len(groups)
    l = 0
    diff = []
    for i in range(1, k):
        diff.append(groups[i][0] - groups[i - 1][1] - 1)
        l += groups[i][1] - groups[i][0] + 1
    if len(groups) > 0:
        l += groups[0][1] - groups[0][0] + 1
    diff.sort()
    mx = k * l
    for i in range(len(groups) - 1):
        k -= 1
        l += diff[i]
        mx = min(mx, k * l)
    print(mx)
