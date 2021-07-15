# Binary Indexed Tree (Fenwick Tree)
class BIT():
    """一点加算、区間取得クエリをそれぞれO(logN)で答える
    add: i番目にvalを加える
    get_sum: 区間[l, r)の和を求める
    i, l, rは0-indexed
    """
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def add(self, i, val):
        """i番目にvalを加える"""
        i = i + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def get_sum(self, l, r):
        """区間[l, r)の和を求める"""
        return self._sum(r) - self._sum(l)


import copy

s = input()
n = len(s)
memo = {}
for i in range(n):
    if s[i] not in memo:
        memo[s[i]] = 1
    else:
        memo[s[i]] += 1

odd_cnt = 0
for i in memo:
    odd_cnt += memo[i] % 2
if odd_cnt > 1:
    print(-1)
    return

left = []
right = []

memo2 = copy.deepcopy(memo)
ans_cnt = 0
word = ""
for i in range(n):
    if memo2[s[i]]*2 > memo[s[i]] + 1:
        memo2[s[i]] -= 1
        ans_cnt += i - len(left)
        left.append(s[i])
    elif memo2[s[i]]*2 == memo[s[i]] + 1:
        word = s[i]
        memo2[s[i]] -= 1
        right.append(s[i])
    else:
        memo2[s[i]] -= 1
        right.append(s[i])
 
if word != "":
    for i in range(len(right)):
        if right[i] == word:
            ans_cnt += i
            del(right[i])
            break
right = right[::-1]

memo = {}
for i in range(len(right)):
    if right[i] not in memo:
        memo[right[i]] = [i]
    else:
        memo[right[i]].append(i)
for i in memo:
    memo[i] = memo[i][::-1]

for i in range(len(left)):
    tmp = left[i]
    left[i] = memo[tmp][-1]
    del(memo[tmp][-1])

memo = {}
for i in range(len(left)):
    memo[i] = left[i]

bit = BIT(len(left))
for i in range(len(left)):
    bit.add(memo[i], 1)
    ans_cnt += bit.get_sum(memo[i] + 1, len(left))
print(ans_cnt)
