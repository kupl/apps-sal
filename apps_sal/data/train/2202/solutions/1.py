class DualBIT():
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def get(self, i):
        '''i番目の要素を取得'''
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def _add(self, i, x):
        while i > 0:
            self.bit[i] += x
            i -= i & -i

    def add(self, i, j, x):
        '''[i, j)の要素にxを加算する'''
        self._add(j, x)
        self._add(i, -x)


n = int(input())
a = list(map(int, input().split()))
                        
bit = DualBIT(n+3)
for i in range(1, n+1):
    bit.add(i+1, n+1, i)

li = []
flag = False
while True:
    if not a:
        break
    ok = n + 1
    ng = 0
    num = a[-1]
    if num == 0 and not flag:
        flag = True
        bit.add(1, n + 2, -1)
        li.append(1)
        del a[-1]
        continue
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if bit.get(mid) > num:
            ok = mid
        else:
            ng = mid
    tmp = ok - 1
    bit.add(ok, n + 2, -tmp)
    li.append(tmp)
    del a[-1]
print(*li[::-1])
          


