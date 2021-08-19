s = input()
t = input()
sm = 0
ss = []
for i in s:
    sm += (i == 'A') * 2 - 1
    ss.append(sm)
ss.append(0)
sm = 0
ts = []
for i in t:
    sm += (i == 'A') * 2 - 1
    ts.append(sm)
ts.append(0)
q = int(input())
for i in range(q):
    inp = list(map(int, input().split()))
    if (ss[inp[1] - 1] - ss[inp[0] - 2]) % 3 == (ts[inp[3] - 1] - ts[inp[2] - 2]) % 3:
        print('YES')
    else:
        print('NO')
