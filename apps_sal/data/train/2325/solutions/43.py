import sys
input = sys.stdin.readline
S = input()
T = input()
SAdata = [int(S[i] == 'A') for i in range(len(S))]
SBdata = [int(S[i] == 'B') for i in range(len(S))]
for i in range(1, len(S)):
    SAdata[i] += SAdata[i - 1]
for i in range(1, len(S)):
    SBdata[i] += SBdata[i - 1]
SAdata.append(0)
SBdata.append(0)
TAdata = [int(T[i] == 'A') for i in range(len(T))]
TBdata = [int(T[i] == 'B') for i in range(len(T))]
for i in range(1, len(T)):
    TAdata[i] += TAdata[i - 1]
for i in range(1, len(T)):
    TBdata[i] += TBdata[i - 1]
TAdata.append(0)
TBdata.append(0)
q = int(input())
for i in range(q):
    (a, b, c, d) = list(map(int, input().split()))
    SA = SAdata[b - 1] - SAdata[a - 2]
    SB = SBdata[b - 1] - SBdata[a - 2]
    TA = TAdata[d - 1] - TAdata[c - 2]
    TB = TBdata[d - 1] - TBdata[c - 2]
    if (SA - SB) % 3 == (TA - TB) % 3:
        print('YES')
    else:
        print('NO')
