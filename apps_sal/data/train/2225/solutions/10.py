
"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc087/tasks/arc087_c

初期状態で出ている数字を木としてあらわす
数字でふさがっている所はもう追加できない
まだおけるのは、空いている部分だけ

Lがでかいので、深さを考えていては死ぬ

そのままふさぐと、置ける場所は1減る
伸ばしておけば、Lまで増やして置ける

置ける場所の偶奇か？
置ける場所が0で来たら負け→初手が奇数なら先手勝ち・そうでないなら後手勝ち？
伸ばせる奴は偶奇反転に使える

部分で考えてみるか→

Grundy数計算
深さ1の部分木のGrundy → 1
深さ2の部分木のGrundy → 2
深さ3　　　　　　　　 → 1 ?
深さ4

Grundyで行ける = xorが全体のGrundyになるという仮定
なので、深さxを試すときは、深さxで1回で行ける状態のxorのmexがGrundyとなる

深さ1なら、問答無用で1
深さ2なら、0 or 1 になるので 2
深さ3なら, 0 or 2 になるので 1
深さ4なら, 0 or 1 or 3 or 2 なので 4
深さ5なら, 0 or 4 or 5 or 7 or 6 で 1
深さ6なら, 0 or 1 or 5 or 4 or 6 or 7 で 2
深さ7なら, 0 or 2 or 3 or 7 or 6 or 4 or 5 で 1
深さ8なら, 0 or 1 or 3 or 2 or 6 or 7 or 5 or 4 で 8

→どうやら、その数字を割り切れる最大の2の階乗数がGrundy数になるみたいだ
つまり、空きポイントを探索して、対応する深さのGrundy数を計算 & xorをとればよい

あとは実装だ
prefix treeを作りたいな？
適当にノードを追加して作ってあげればいいか
保持するデータは、0の子index,1の子index,深さがあれば十分かな
計算量がちょっと気になるところ(再帰はなるべく避けたいところ)

"""

def tp_z(now , nd):

    if z_child[now] == None:
        ret = len(z_child)
        z_child[now] = ret
        z_child.append(None)
        o_child.append(None)
        dep.append(nd + 1)
    else:
        ret = z_child[now]

    return ret

def tp_o(now , nd):

    if o_child[now] == None:
        ret = len(z_child)
        o_child[now] = ret
        z_child.append(None)
        o_child.append(None)
        dep.append(nd + 1)
    else:
        ret = o_child[now]

    return ret

def grundy(nd):

    if nd == 0:
        return 0

    for i in range(64):
        if nd % (2**i) != 0:
            return 2**(i-1)
        

N,L = map(int,input().split())

z_child = [None]
o_child = [None]
dep = [0]

for loop in range(N):

    now = 0
    s = input()

    for i in s:
        if i == "0":
            now = tp_z(now , dep[now])
        else:
            now = tp_o(now , dep[now])

#print (z_child)
#print (o_child)
#print (dep)

ans = 0
for i in range(len(z_child)):

    if z_child[i] == None:
        ans ^= grundy(L - dep[i])
    if o_child[i] == None:
        ans ^= grundy(L - dep[i])

if ans == 0:
    print ("Bob")
else:
    print ("Alice")
