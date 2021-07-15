from collections import Counter


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


def min_swap_times(s, t):
    if Counter(s) != Counter(t):
        return -1

    n = len(s)
    memo = {}
    for i in range(n):
        if s[i] not in memo:
            memo[s[i]] = [i]
        else:
            memo[s[i]].append(i)
    for i in memo:
        memo[i] = memo[i][::-1]

    array = [0] * n
    for i in range(n):
        array[i] = memo[t[i]][-1]
        del(memo[t[i]][-1])    

    memo = {}
    for i in range(n):
        memo[i] = array[i]
    bit = BIT(n)
    res = 0

    for i in range(n):
        bit.add(memo[i], 1)
        res += bit.get_sum(memo[i] + 1, n)
    return res


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
tmp = min_swap_times(left, right)
if tmp == -1:
    print(-1)
else:
    print(ans_cnt + tmp)
