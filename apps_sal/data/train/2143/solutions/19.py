n, c, d = list(map(int, input().split()))
coin = []
diamond = []
for i in range(n):
    tmp = input().split()
    if tmp[-1] == 'C' and int(tmp[1]) <= c:
        coin.append(list(map(int, tmp[:2])))
    if tmp[-1] == 'D' and int(tmp[1]) <= d:
        diamond.append(list(map(int, tmp[:2])))
res1 = 0
mc = -float('inf')
for i in coin:
    if mc < i[0] and i[1] <= c:
        mc = i[0]
md = -float('inf')
for i in diamond:
    if md < i[0] and i[1] <= d:
        md = i[0]
if mc != -float('inf') and md != -float('inf'):
    res1 = md + mc
coin.sort(key=lambda x: x[1], reverse=True)
diamond.sort(key=lambda x: x[1], reverse=True)
prefc = [0 for i in range(len(coin))]
prefd = [0 for i in range(len(diamond))]
if len(coin):
    prefc[-1] = coin[-1][0]
if len(diamond):
    prefd[-1] = diamond[-1][0]
for i in range(len(coin) - 2, -1, -1):
    prefc[i] = max(prefc[i + 1], coin[i][0])
for i in range(len(diamond) - 2, -1, -1):
    prefd[i] = max(prefd[i + 1], diamond[i][0])
res2 = 0
res3 = res2
for i in range(len(coin)):
    p = c - coin[i][1]
    l = i
    r = len(coin) - 1
    while r - l > 1:
        m = (r + l) // 2
        if coin[m][1] > p:
            l = m
        else:
            r = m
    if coin[r][1] <= p and r > i:
        res2 = max(res2, coin[i][0] + prefc[r])
for i in range(len(diamond)):
    p = d - diamond[i][1]
    l = i
    r = len(diamond) - 1
    while r - l > 1:
        m = (r + l) // 2
        if diamond[m][1] > p:
            l = m
        else:
            r = m
    if diamond[r][1] <= p and r > i:
        res3 = max(res3, diamond[i][0] + prefd[r])
print(max(res1, res2, res3))

