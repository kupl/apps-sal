# N、Lの入力受付
N, L = list(map(int, input().split()))
# N回連続で入力文字列を受付
S = []
for i in range(N):
    S.append(input())
# S内をソート
S.sort()
# Sの要素を結合
result = ""
for i in range(N):
    result = result + S[i]
# resultを出力
print(result)

