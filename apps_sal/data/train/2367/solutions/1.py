from operator import itemgetter


class BIT:

    def __init__(self, n):
        """n = 要素数
        要素の添字iは 0 <= i < n となる
        """
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, i, val):
        """i番目の要素にvalを加算する O(logN)"""
        i = i + 1
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def _sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & -i
        return s

    def sum(self, i, j):
        """区間[i, j)の和を求める O(logN)"""
        return self._sum(j) - self._sum(i)


def run_length_compress(string):
    string.append('@')
    n = len(string)
    begin = 0
    end = 1
    cnt = 1
    ans = []
    while True:
        if end >= n:
            break
        if string[begin] == string[end]:
            end += 1
            cnt += 1
        else:
            ans.append((cnt, string[begin]))
            begin = end
            end = begin + 1
            cnt = 1
    return ans


q = int(input())
for _ in range(q):
    n = int(input())
    s = list(input())
    t = list(input())
    tmp_s = sorted(s)
    tmp_t = sorted(t)
    s_run = run_length_compress(tmp_s)
    t_run = run_length_compress(tmp_t)
    flag = False
    f = False
    for i in range(len(s_run)):
        if s_run[i][0] >= 2:
            flag = True
        if s_run[i] != t_run[i]:
            print('NO')
            f = True
            break
    if f:
        continue
    if flag:
        print('YES')
        continue
    cnt_s = 0
    cnt_t = 0
    for i in range(n)[::-1]:
        for j in range(i):
            if s[j] > s[j + 1]:
                (s[j], s[j + 1]) = (s[j + 1], s[j])
                cnt_s += 1
            if t[j] > t[j + 1]:
                (t[j], t[j + 1]) = (t[j + 1], t[j])
                cnt_t += 1
    if cnt_s % 2 == cnt_t % 2:
        print('YES')
    else:
        print('NO')
