H, W = list(map(int, input().split()))
ans = max(H, W)
S = [input() for i in range(H)]
T = [[0] * (W - 1)]
for i in range(H - 1):
    t, ts = [], []
    for j in range(W - 1):
        r = S[i][j:j + 2] + S[i + 1][j:j + 2]
        t.append(r.count('.') % 2)
        if t[j] == 0:
            ts.append(T[-1][j] + 1)
        else:
            ts.append(0)
    T.append(ts)
for L in T[1:]:
    stack = []
    for i, l in enumerate(L + [0]):
        w = -1
        while stack and stack[-1][1] >= l:
            w, h = stack.pop()
            ans = max(ans, (h + 1) * (i - w + 1))
        if w != -1:
            stack.append((w, l))
            continue
        stack.append((i, l))
print(ans)
