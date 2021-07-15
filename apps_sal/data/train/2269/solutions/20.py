"""
E問題
繋がっている都市同士は同じ州にあっても違う州にあってもよい→考えにくい
→「繋がっていない都市は必ず違う州にある」のほうが考えやすい
→繋がっていない都市にすべて辺を張って二部グラフが構成できるかどうかで判定できそう？
（必要条件ではあるけど十分条件であるかどうかはわからない）
→この条件だと同じ州にあるなら必ず任意の二都市間は繋がっているので十分条件も満たしてそう！
（∵繋がっていない都市に辺を張った時同じ州内に辺を持たないため）

（繋がっていない都市に辺を張った）グラフが連結⇒都市の選び方は高々1通り
連結でないなら複数の選び方が存在する
→最小となるような選び方はどのように決めればよいか？
→それぞれの連結成分ごとに、片方にai都市、もう片方にbi都市振り分けられるとすると
L = [[a1, b1], [a2, b2], ... , [ak, bk]]
とできて、(sum(A)+sum(B) == n)
s = Σ[i = 1 to k](aiかbiのどちらかを選んで足す)　としたときに
もっともsがn//2に近くなるようにsを選べばよく、これはdpでO(nk)でできる
"""
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)
import numpy as np

n, m = map(int, input().split())
G = [{i for i in range(n) if i != j} for j in range(n)]
for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  G[a].remove(b)
  G[b].remove(a)

seen = [-1]*n
L = []
def is_bipartite(v, color):
  seen[v] = color
  L[-1][color] += 1
  for i in G[v]:
    if seen[i] != -1:
      if seen[i] == color:
        return False
    else:
      if not is_bipartite(i, color^1):
        return False
  return True

for i in range(n):
  if seen[i] == -1:
    L.append([0, 0])
    if not is_bipartite(i, 0):
      print(-1)
      break
else:
  dp = np.zeros((len(L)+1, n+1), dtype=bool)
  dp[0, 0] = True
  for i, ab in enumerate(L):
    a, b = ab
    dp[i+1, a:] |= dp[i, :n+1-a]
    dp[i+1, b:] |= dp[i, :n+1-b]
  temp = n//2
  dp = dp[-1].tolist()
  while not dp[temp]:
    temp += 1
  r = n - temp
  print(temp*(temp-1)//2 + r*(r-1)//2)
