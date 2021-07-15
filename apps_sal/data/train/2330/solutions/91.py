import sys
def LI2(): return list(map(int,sys.stdin.readline().rstrip()))  #空白なし


S = LI2()
n = len(S)

if S[-1] == 1 or S[0] == 0 or S[-2] == 0:
    print((-1))
    return

for i in range(n-1):
    if S[i] != S[-2-i]:
        print((-1))
        return


k = S.count(1)  # 1の個数
for i in range(k):
    print((i+1,i+2))

a = 1  # 付け足す辺の端点
b = k+2  # 付け足す頂点のindex
for i in range(n-1):
    if S[i] == 1:
        a += 1
    else:
        print((a,b))
        b += 1

