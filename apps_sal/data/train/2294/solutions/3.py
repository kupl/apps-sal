import sys
input = sys.stdin.readline
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
for i in range(n):
    l[i].sort()

ans = []
l.sort()
B1 = []
R1 = []
for i in range(n):
    B1.append(max(l[i]))
    R1.append(min(l[i]))
ans.append((max(B1) - min(B1)) * (max(R1) - min(R1)))

Bleft = []
Bright = []
Rleft = []
Rright = []

M = B1[0]
m = B1[0]
Bleft.append([m, M])
for i in range(1, n):
    M = max(M, B1[i])
    m = min(m, B1[i])
    Bleft.append([m, M])

B1.reverse()
M = B1[0]
m = B1[0]
Bright.append([m, M])
for i in range(1, n):
    M = max(M, B1[i])
    m = min(m, B1[i])
    Bright.append([m, M])

M = R1[0]
m = R1[0]
Rleft.append([m, M])
for i in range(1, n):
    M = max(M, R1[i])
    m = min(m, R1[i])
    Rleft.append([m, M])

R1.reverse()
M = R1[0]
m = R1[0]
Rright.append([m, M])
for i in range(1, n):
    M = max(M, R1[i])
    m = min(m, R1[i])
    Rright.append([m, M])

for i in range(n - 1):
    M1 = max(Bleft[i][1], Rright[n - 2 - i][1])
    m1 = min(Bleft[i][0], Rright[n - 2 - i][0])
    M2 = max(Rleft[i][1], Bright[n - 2 - i][1])
    m2 = min(Rleft[i][0], Bright[n - 2 - i][0])
    ans.append((M1 - m1) * (M2 - m2))

print(min(ans))
