import sys
N, M = list(map(int, input().split()))

I = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    I[a][b] = 1
    I[b][a] = 1
for a in range(N):
    I[a][a] = 1
# 0を辺とするグラフが二部グラフか否か判定
#print(*I, sep="\n")

# 各連結成分の頂点数
R = []
B = []

vis = set()


def dfs(s, c):  # 0を辺とするグラフが二部グラフか否かを、始点s, 初期色cのBFSで判定
    adj = I[s]
    tmp = True
    r_ct = 0
    b_ct = 0
    clr[s] = c
    for p in range(N):
        if adj[p] == 1:  # 隣接してない
            continue
        if p in vis:
            if clr[p] != 1 - c:
                #print(s, p)
                return False
            continue
        else:
            vis.add(p)
            if not dfs(p, 1 - c):
                return False
    return True


# 二部グラフかいなかと、各連結成分の色ごとの数を判定
vis = set()
ans = 0
used_edge = 0
for s in range(N):
    if s in vis:
        continue
    R.append(0)
    B.append(0)
    clr = {}
    vis.add(s)
    if not dfs(s, 0):
        print((-1))
        return
    # print(clr)
    for p in clr:
        if clr[p] == 0:
            R[-1] += 1
        else:
            B[-1] += 1
    for p in clr:
        for q in clr:
            if p != q and I[p][q] == 1:
                used_edge += 1
                if clr[p] == clr[q]:
                    ans += 1
    # print(ans)

# print(R)
# print(B)

# 最大値 : a_i*b_jの非対角和の半分で、a_iの和がN/2に最も近い場合
DP = 1
for i in range(len(R)):
    DP = (DP << R[i]) | (DP << B[i])

i = 0
ex = []
while DP > 0:
    if DP % 2 == 1:
        ex.append(i)
    i += 1
    DP >>= 1
# print(ex)
ex.sort(key=lambda x: abs(2 * x - N))
# print(ex[0])
tmp = ex[0] * (N - ex[0])
for i in range(len(R)):
    tmp -= R[i] * B[i]
# print(used_edge)
# print(tmp)
#print(2*M - used_edge)
ans //= 2
ans += (2 * M - used_edge) // 2 - tmp

print(ans)
