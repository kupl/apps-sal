
"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc081/tasks/arc081_c

1文字がありうるのは、出てない文字があるとき
2文字がありうるのは、全ての文字が1度出たのち、もう一度すべての文字が1度現れてない場合
つまり答えの文字数はこの方法で分かる

では辞書順最小のものは？
k文字であることがわかっていたとする。
この時、どの文字も最低k-1回出現している
最後の文字は、k回出現してない文字の内、辞書順最小の物
最後から1番目は、k-1回目の出現の後、最後の文字が出ていない者
最後から2番目は、

abcの3文字しかないとする
abababababcab

→この時、求めるのは、?cで、?はc最後に出現するcよりも前に存在しないk-1文字の辞書順最小

abcabcab
→??c
→最後の出現するc以前=abcab以前で存在しない2文字
→?cc
→abで存在しない1文字
→ccc

acbaccbac
→結局再帰的に解ける
→出現回数が最小の文字のうち、辞書順最小の物を答えの最後の文字から決めていき、その文字が最後の出現したind
より前に関して、同じ問題を解く

あとはどうやって計算量を削減するか
その時点で、どの文字が何度出たか、最後の出現したindexはどこか、を記録して置いて再帰的に解く

→方針は合ってる？けど実装してるのが違うよ！
保存しておくのは、全ての文字が何回出揃ったか、とその後どの文字が出ているか。
&各文字が最後にどこで出たか。

あれー？
aaaaaabbbbbbc

→問題は、必ずしも後ろから最適なのを選んで行けばいいわけではなかったこと
→これはあくまで、後ろから見て辞書順最小でしかない…あれまさか？
→正解しちゃったー？？？
"""

A = list(input())
A.reverse()

alp = "abcdefghijklmnopqrstuvwxyz"
alpdic = {}
for i in range(26):
    alpdic[alp[i]] = i

allcol = [0] * (len(A) + 1)
apnum = [[0] * 26 for i in range(len(A) + 1)]
lastap = [[0] * 26 for i in range(len(A) + 1)]

for i in range(len(A)):

    for j in range(26):
        apnum[i + 1][j] = apnum[i][j]
        lastap[i + 1][j] = lastap[i][j]
        allcol[i + 1] = allcol[i]

    apnum[i + 1][alpdic[A[i]]] |= 1
    if 0 not in apnum[i + 1]:
        apnum[i + 1] = [0] * 26
        allcol[i + 1] += 1
    lastap[i + 1][alpdic[A[i]]] = i + 1

anslen = allcol[-1] + 1
ans = []
nind = len(A)

for i in range(anslen):

    minind = 0
    for j in range(26):
        if apnum[nind][j] == 0:
            minind = j
            break
    ans.append(alp[minind])

    nind = lastap[nind][minind] - 1

print("".join(ans))
