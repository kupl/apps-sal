(n, q) = list(map(int, input().split()))
a = list(map(int, input().split()))
k = max(a)
spe = a.index(k)
pre = []
fol = []
board = []
tem = a[0]
i = 1
while i <= spe:
    pre.append([tem, a[i]])
    if tem > a[i]:
        fol.append(a[i])
    else:
        fol.append(tem)
        tem = a[i]
    i += 1
board = a[spe:]
board.extend(fol)
for _ in range(q):
    m = int(input())
    if m <= spe:
        print(pre[m - 1][0], pre[m - 1][1])
    else:
        m = (m - spe) % (n - 1)
        if m == 0:
            m = n - 1
        print(k, board[m])
