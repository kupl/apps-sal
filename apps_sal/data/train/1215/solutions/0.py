def isSolvable(W, R):
    (LW, LR, F, ML, AW, V, LMap) = (len(W), len(R), set([w[0] for w in W + [R]]), max(map(len, W + [R])), W + [R], set(), {})
    if LR < ML:
        return False

    def dfs(d, i, c):
        if d == ML:
            return c == 0
        if i == len(W) + 1:
            s = sum((LMap[w[-d - 1]] if d < len(w) else 0 for w in W)) + c
            return dfs(d + 1, 0, s // 10) if s % 10 == LMap[R[-d - 1]] else False
        if i < LW and d >= len(W[i]):
            return dfs(d, i + 1, c)
        ch = AW[i][-d - 1]
        if ch in LMap:
            return dfs(d, i + 1, c)
        for x in range(ch in F, 10):
            if x not in V:
                (LMap[ch], _) = (x, V.add(x))
                if dfs(d, i + 1, c):
                    return True
                V.remove(LMap.pop(ch))
    return dfs(0, 0, 0)


n = int(input())
W = []
for i in range(n):
    W.append(str(input()))
R = input()
a = isSolvable(W, R)
if a == True:
    print('true')
else:
    print('false')
