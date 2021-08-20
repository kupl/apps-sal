def inpl():
    return [int(i) for i in input().split()]


(H, W) = inpl()
ans = max(H, W)
S = [input() for _ in range(H)]
T = [[0] * (W - 1)]
for i in range(H - 1):
    t = []
    for j in range(W - 1):
        r = S[i][j:j + 2] + S[i + 1][j:j + 2]
        t.append(r.count('.') % 2)
    ts = [T[-1][i] + 1 if not k else 0 for (i, k) in enumerate(t)]
    T.append(ts)
for iT in T[1:]:
    stack = []
    for (i, l) in enumerate(iT + [0]):
        dw = -1
        while stack and stack[-1][1] >= l:
            (dw, dh) = stack.pop()
            ans = max(ans, (dh + 1) * (i - dw + 1))
        if dw != -1:
            stack.append((dw, l))
            continue
        stack.append((i, l))
print(ans)
