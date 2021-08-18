"""
まず、奇数個存在する文字種が複数ある場合は、回文にできない。
それ以外の場合は、回文にできる。
次に、操作の最小回数は、回文になった場合の各文字のインデックスを求めておき、BITを使って、入れ替えが必要な回数を求めて置く
"""
from collections import Counter
S = input()
N = len(S)
# 各文字の出現回数をカウント
apperance = Counter(S)

# 回文を作成できるか判定
flag = False
for k, v in list(apperance.items()):
    if v % 2 == 1:
        if flag:
            print((-1))
            return
        else:
            flag = True
            t = k


# place[s] -> 文字sの出現位置
place = {}
for i in range(N):
    s = S[i]
    if s not in place:
        place[s] = []
    place[s].append(i)

# memo[i] -> Sのi文字目の回文上でのインデックス
memo = [-1] * (N)

# 回文前半、後半に含まれることになる文字に、回文上でのインデックスを割り当てる。
tmp = 0
tmpApperance = {}
for i in range(N):
    s = S[i]
    if s not in tmpApperance:
        tmpApperance[s] = 1
    else:
        tmpApperance[s] += 1
    if tmpApperance[s] <= apperance[s] // 2:
        memo[i] = tmp
        backIdx = place[s][-tmpApperance[s]]
        memo[backIdx] = N - tmp - 1
        tmp += 1


# 回文の真ん中に含まれることになる文字に、回文上でのインデックスを割り当てる。
if flag:
    idx = N // 2
    memo[place[t][len(place[t]) // 2]] = idx


class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i


bit = BIT(N)
cnt = 0
for i in range(N):
    m = memo[i] + 1
    bit.add(m, 1)
    cnt += bit.sum(N) - bit.sum(m)

print(cnt)
