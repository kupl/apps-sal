"""
回文の左半分の文字列たちを操作する。
左半分の各文字に対して、本来あるべき場所(Index)を定義する。
あとは、左半分の文字

"""

from collections import Counter


class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):  # 1-index
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):  # 1-index
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


S = input()
N = len(S)
count = Counter(S)

# 奇数個ある文字が複数存在していないかチェック
flag = False
for v in list(count.values()):
    if v % 2 == 1:
        if flag:
            print((-1))
            return
        else:
            flag = True

# 各文字が属すべきインデックスを求める
# memo[i] -> S[i]の回文変換後のインデックス(0-indexed)
memo = [None] * (N)
# appearCnt[k] -> 文字kの出現回数
appearCnt = {k: 0 for k in list(count.keys())}

# まず、回文時に左半分に属する文字に関して、インデックスを割り当てる。
tInd = 0
for i in range(N):
    s = S[i]
    if appearCnt[s] <= count[s] // 2 - 1:
        appearCnt[s] += 1
        memo[i] = tInd
        tInd += 1

# 奇数個ある文字がある場合は、真ん中になる文字に関して、インデックスを割り当てる
if flag:
    for i in range(N):
        s = S[i]
        if count[s] % 2 == 1 and memo[i] == None:
            memo[i] = tInd
            break

# 回文時に右半分になる文字にインデックスを割り当てる。
# まず、各文字の文字列Sにおける出現回数をまとめる
appearIdx = {k: [] for k in list(count.keys())}
for i in range(N):
    s = S[i]
    appearIdx[s].append(i)

for v in list(appearIdx.values()):
    for i in range(len(v) // 2):
        l = v[i]
        r = v[len(v) - i - 1]
        memo[r] = (N - 1) - memo[l]
ans = 0
bit = BIT(N)
for i in range(N):
    bit.add(memo[i] + 1, 1)
    ans += bit.sum(N) - bit.sum(memo[i] + 1)
print(ans)
