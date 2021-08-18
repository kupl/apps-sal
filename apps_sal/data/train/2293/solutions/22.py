
"""

https://atcoder.jp/contests/arc100/tasks/arc100_c

情報を再利用するのがメイン
K=Xの時は,K=X-1の時の答えに加え、 i or j == K の場合を考えればいい
or がKとなる場合、0の桁は両方0で、1の桁は片方が1ならよい
1では3通りの分け方があるので、3^N…

大きいほうから考えてみる？
最後は、当然最大のやつ2個→その2つのindex のORまではそれが保持

dp[X] = X と orしてもXのままのindexの集合における最大 & 2番目
→とすれば、1の桁全てに関して0にしてみた奴とXを見れば推移できる

O(2^N * logMAX(A)) で解けそうだ

"""

from sys import stdin

N = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
A.append(float("-inf"))

dp = []
ans = 0
aaa = []

for i in range(2**N):

    if i == 0:
        dp.append((0, -1))
        continue

    na, nb = i, -1

    for j in range(N):

        if (2**j) & i > 0:

            ta, tb = dp[i ^ (2**j)]
            if A[na] < A[ta]:
                nb = na
                na = ta
            elif A[nb] < A[ta] and ta != na:
                nb = ta

            if A[nb] < A[tb]:
                nb = tb

    ans = max(A[na] + A[nb], ans)
    aaa.append(ans)
    dp.append((na, nb))

print(("\n".join(map(str, aaa))))
