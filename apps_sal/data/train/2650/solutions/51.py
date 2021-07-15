#NとLを入力
N, L = map(int, input().split())


# 空のリストを生成
S = []

#入力
for i in  range(N):
    array = input()
    S.append(array)

#辞書順に並べ替え
S.sort()

#pythonのリストの出力では[と,が出力されるので取る
S=''.join(S)

#出力
print(S)
