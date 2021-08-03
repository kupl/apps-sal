
"""

石の数が最大の内数字が大きいものから取り除いていくのが最適？

前にあるできるだけ数が多いものに譲っていく

優先度付きキューでaが大きい方からpopしていく？

numが現在より小さい→以降する
そうでない = 現在のnumよりは低いが次のnumよりは大きい
→次のnumが確定した瞬間に差分を計算して定常減少用に入れる

最後は残りを全部1に入れて終わり
"""
import heapq

N = int(input())

ans = [0] * N

a = list(map(int, input().split()))

q = []

for i, na in enumerate(a):

    heapq.heappush(q, [-1 * na, i])

nowa, nowi = heapq.heappop(q)
nowa *= -1
always = 0
tempq = [nowa]

for i in range(N - 1):

    nexa, nexi = heapq.heappop(q)
    nexa *= -1

    if nexi > nowi:
        tempq.append(nexa)

    else:
        nowpl = always * (nowa - nexa)

        for j in tempq:
            nowpl += j - nexa

        always += len(tempq)
        tempq = [nexa]

        ans[nowi] += nowpl

        nowa = nexa
        nowi = nexi

ans[0] = sum(a) - sum(ans)

print("\n".join(map(str, ans)))
