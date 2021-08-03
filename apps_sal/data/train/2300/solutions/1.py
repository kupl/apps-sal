
"""

https://atcoder.jp/contests/arc086/tasks/arc086_c

対消滅する可能性があるのは同じ深さの点に置かれたビー玉だけ
→1つも残らない or 1つだけ残るである

すなわち、ある深さに関して、そのうち1つ残るのがいくつあるかを数えればよい

1つだけ置く場合→絶対のこる
2つ置く場合→絶対消える
3つ置く場合→3つのLCAが等しくなければ残る

木dpみたいにする？
dp[0] = 一つも含んでいない場合の通り数
dp[1] = 1つ含んでいる場合の通り数

dp[0] = すべての場合 - dp[1]
dp[1] = 1つだけ1を持っている場合

で、子から親に伝播させていく…？
マージテクで計算量削減か？
3sだからそうっぽいな…
3つ以上のマージ書くのだるすぎん？

またはマージの順番をどっかにメモっておく

maxd-d = indexでやる
最長のやつにマージする

dp[maxd-d][1] = 1つだけ元深さdが残っている場合の数
c = 子の数

計算量は？
サイズは高々1しか増えないので可能っぽい
2倍処理がまずい

もっと簡潔に？
単一のdだけで考えよう
2倍処理なんてしない
最後に各dに関してかければいい
→するとマージの際に2番目の大きさだけでなんとかなる

必要のないマージをしない
両方に関係ないdは操作しない
むしろばらつきは深い部分にだけ存在するか
浅い部分は共通。よって-xで管理すればいいか

"""

from collections import deque
import sys
mod = 10**9 + 7
sys.setrecursionlimit(200000)


def NC_Dij(lis, start):

    ret = [float("inf")] * len(lis)
    ret[start] = 0

    q = deque([start])
    plis = [i for i in range(len(lis))]

    while len(q) > 0:
        now = q.popleft()

        for nex in lis[now]:

            if ret[nex] > ret[now] + 1:
                ret[nex] = ret[now] + 1
                plis[nex] = now
                q.append(nex)

    return ret, plis


def inverse(a):  # aのmodを法にした逆元を返す
    return pow(a, mod - 2, mod)


def dfs(v):

    if len(lis[v]) == 0:
        ret = [[1, 1]]
        return ret

    else:

        retlis = []
        for nex in lis[v]:
            nret = dfs(nex)
            retlis.append([len(nret), nret])
        retlis.sort()

        # 1つしかない場合マージしない
        if len(retlis) == 1:
            retlis[-1][1].append([1, 1])
            return retlis[-1][1]

        # 2つ以上の場合最大のやつにマージする
        for revd in range(retlis[-2][0]):

            zmul = 1
            amul = 1
            for i in range(len(retlis) - 1, -1, -1):
                if revd < retlis[i][0]:
                    zmul *= retlis[i][1][-1 - revd][0]
                    amul *= sum(retlis[i][1][-1 - revd])
                    zmul %= mod
                    amul %= mod
                else:
                    break

            nsum = 0
            for i in range(len(retlis) - 1, -1, -1):
                if revd < retlis[i][0]:
                    nsum += zmul * inverse(retlis[i][1][-1 - revd][0]) * retlis[i][1][-1 - revd][1]
                    nsum %= mod
                else:
                    break

            retlis[-1][1][-1 - revd][1] = nsum
            retlis[-1][1][-1 - revd][0] = (amul - nsum) % mod

        retlis[-1][1].append([1, 1])
        return retlis[-1][1]


N = int(input())
p = list(map(int, input().split()))

lis = [[] for i in range(N + 1)]

for i in range(N):

    # lis[i+1].append(p[i])
    lis[p[i]].append(i + 1)

dlis, plis = NC_Dij(lis, 0)
maxd = max(dlis)

dn = [0] * (maxd + 1)
for i in dlis:
    dn[i] += 1

ans = dfs(0)
#print (dn,ans)
A = 0
for i in range(maxd + 1):
    A += ans[-1 - i][1] * pow(2, N + 1 - dn[i], mod)
    A %= mod
print(A)
