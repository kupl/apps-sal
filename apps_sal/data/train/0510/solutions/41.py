"""
AtCoder Beginner Contest 157  E - Simple String Queries

文字列Sに対して、
クエリ1：i番目の文字をcに変更
クエリ2：S[l~r]に何種類の文字があるか

各クエリについて、律儀に文字を変えて、l~rについて何種類あるか調べると間に合わないはず。

~~~ABCCDC~~~
        ↑を別の文字にした時に、最後に出てくるCがその二個左、のような情報をちゃんと残したい。
→ 最後の位置が知りたいとかではなく、lとrを指定した時に、その間にあるかが知りたい（具体的な位置が知りたいわけではない）
　そうするt、a〜zについて、l~rに存在するか、みたいな確認ができそう

N <= 5 * 10**5
Q <= 2 * 10**4
なので、bisect使えば間に合うのか？よくわからん

Sとしてではなく、現時点で何文字目がなになのかも持っておいたほうが楽か。

"""

import bisect

N = int(input())
S = input()
Q = int(input())

cS = [""] * N
char_idxs = [[]for _ in range(26)]

for i, s in enumerate(S):
    cS[i] = s
    char_idxs[ord(s) - 97].append(i)

query = [tuple(map(str, input().split())) for _ in range(Q)]


for q, a, b in query:

    if q == "1":
        if cS[int(a) - 1] == b:
            continue
        else:

            idx = bisect.bisect_right(char_idxs[ord(cS[int(a) - 1]) - 97], int(a) - 1)
            if char_idxs[ord(cS[int(a) - 1]) - 97][idx - 1] == int(a) - 1:
                char_idxs[ord(cS[int(a) - 1]) - 97][idx - 1:idx] = []

            bisect.insort_right(char_idxs[ord(b) - 97], int(a) - 1)

            cS[int(a) - 1] = b

    else:
        cnt = 0
        for i in range(26):
            if len(char_idxs[i]) == 0:
                continue
            l = bisect.bisect_left(char_idxs[i], int(a) - 1)

            if l < len(char_idxs[i]) and char_idxs[i][l] <= int(b) - 1:
                cnt += 1

        print(cnt)
