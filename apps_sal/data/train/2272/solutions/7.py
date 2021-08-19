
"""

https://atcoder.jp/contests/arc092/tasks/arc092_b

桁における1の数の偶奇だけで決まる
1+1 -> 0 (1繰り上がり)
1+0 -> 1
0+0 -> 0
なので、1の位においてはそう

2の位では？繰り上がりがある
繰り上がりも含めて、1がいくつあるかわかればいい
その桁への繰り上がりがあるかは、二分探索でわかるはず

200000*28*log

"""

from sys import stdin
import bisect

N = int(stdin.readline())
a = list(map(int, stdin.readline().split()))
b = list(map(int, stdin.readline().split()))

ans = 0

for i in range(29):

    ndig = 2**i
    now = 0

    for j in a:
        if j & ndig > 0:
            if N % 2 == 1:
                now ^= 1
    for j in b:
        if j & ndig > 0:
            if N % 2 == 1:
                now ^= 1

    nb = [j % ndig for j in b]
    nb.sort()
    nb.reverse()
    #print (now)

    for j in a:

        na = j % ndig
        l = -1
        r = N

        while r - l != 1:
            m = (l + r) // 2
            if nb[m] + na < ndig:
                r = m
            else:
                l = m

        if r % 2 == 1:
            now ^= 1

    ans += now * ndig

print(ans)
