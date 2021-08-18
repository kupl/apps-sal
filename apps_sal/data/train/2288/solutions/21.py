
"""
Writer: SPD_9X2
https://atcoder.jp/contests/arc082/tasks/arc082_d

aiが固定ならば、ただクエリをソートしてシミュレーションしながら答えを出せばよい
今回はそうでないので、方法を考える

一度でも砂が落ち切ってしまえば、その後はaiに関わらず、答えは等しくなる
おちきっていない場合、常に砂が移動し続けるので、初期値からの差分が常に等しくなる
よって、落ち切らないaの範囲を保持し、一度も落ち切らない場合の初期からの差分
& 落ち切ってしまった場合のシミュレーション結果を用いて答えればよい

→どのタイミング(区間)で落ち切るかでその後の動きが違くね？？？
→死

→aの区間は高々3つに分けられる
→ aが少なく、a=0と同じに収束する場合、 aが大きく、a=Xと同じに収束する場合。、一度も落ち切らない場合
→そして、a=0,a=Xと同じになる場合は、それぞれaの初期値の区間の両端から侵食していく
→よって、a=0のシミュ、a=Xのシミュ、落ち切らない差分シミュ。その時あるaがどれに属すかの区間
を用いてシミュレーションしながらdp的に処理してあげればよい

あとは実装が面倒そう
"""
from collections import deque
X = int(input())
K = int(input())

r = list(map(int, input().split()))
r.append(float("inf"))
r.append(0)

ta = deque([])
Q = int(input())

for i in range(Q):
    t, a = list(map(int, input().split()))
    ta.append([t, a])

ZA = 0
XA = X
D = 0
Zmax = 0
Xmin = X

for i in range(K + 1):

    time = r[i] - r[i - 1]

    if i % 2 == 0:

        while len(ta) > 0 and ta[0][0] <= r[i]:
            t, a = ta.popleft()
            td = t - r[i - 1]

            if a <= Zmax:
                print((max(0, ZA - td)))
            elif a >= Xmin:
                print((max(0, XA - td)))
            else:
                print((max(0, a + D - td)))

        D -= time
        Zmax = max(Zmax, -1 * D)
        ZA = max(0, ZA - time)
        XA = max(0, XA - time)

    else:

        while len(ta) > 0 and ta[0][0] <= r[i]:
            t, a = ta.popleft()
            td = t - r[i - 1]

            if a <= Zmax:
                print((min(X, ZA + td)))
            elif a >= Xmin:
                print((min(X, XA + td)))
            else:
                print((min(X, a + D + td)))

        D += time
        Xmin = min(Xmin, X - D)
        ZA = min(X, ZA + time)
        XA = min(X, XA + time)
