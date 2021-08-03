import sys
sys.setrecursionlimit(1000000)


def getGrundyNumber(x):
    ans = 1
    while x % (ans * 2) == 0:
        ans *= 2
    return ans


def dfs(iT, Hgt):
    num = 0
    for c in Trie[iT]:
        if c != -1:
            dfs(c, Hgt - 1)
            num += 1

    if num == 1:
        Hgts[Hgt - 1] = Hgts.get(Hgt - 1, 0) + 1


N, L = list(map(int, input().split()))
Ss = [input() for i in range(N)]

# トライ木を作成する
Trie = [[-1, -1]]
for S in Ss:
    iT = 0
    for c in map(int, S):
        if Trie[iT][c] == -1:
            Trie += [[-1, -1]]
            Trie[iT][c] = len(Trie) - 1
        iT = Trie[iT][c]

# 子が１つの頂点を探す
Hgts = {}
dfs(0, L + 1)

# Grundy数のXORを求める
ans = 0
for Hgt, num in list(Hgts.items()):
    if num % 2:
        ans ^= getGrundyNumber(Hgt)

if ans:
    print('Alice')
else:
    print('Bob')
