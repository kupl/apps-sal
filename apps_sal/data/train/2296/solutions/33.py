class BIT:
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


def swap_time(array0, array1):
    n = len(array0)
    memo = {}
    for i in range(n)[::-1]:
        if array0[i] not in memo:
            memo[array0[i]] = []
        memo[array0[i]].append(i)
    res = []
    for val in array1:
        ind = memo[val].pop()
        res.append(ind)

    bit = BIT(n)
    ans = 0
    for i in range(n):
        bit.add(res[i], 1)
        ans += bit.get_sum(res[i] + 1, n)
    return ans


ALPH = "abcdefghijklmnopqrstuvwxyz"
s = input()

cnt_memo = {}
for char in s:
    if char not in cnt_memo:
        cnt_memo[char] = 1
    else:
        cnt_memo[char] += 1

odd = ""
for char in cnt_memo:
    if cnt_memo[char] % 2 == 1:
        if odd:
            print(-1)
            return
        else:
            odd = char
            cnt_memo[char] -= 1
            cnt_memo[char] //= 2
    else:
        cnt_memo[char] //= 2

left = []
mid = []
if odd:
    mid = [odd]
right = []
for char in s:
    if odd == char and cnt_memo[char] == 0:
        odd = ""
    elif cnt_memo[char] != 0:
        left.append(char)
        cnt_memo[char] -= 1
    else:
        right.append(char)

ans = 0
ans += swap_time(left + mid + right, list(s))
ans += swap_time(left, right[::-1])
print(ans)
