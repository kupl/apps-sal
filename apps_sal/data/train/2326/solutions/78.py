import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

B = [[A[i], i] for i in range(n)]
B.sort(key=lambda x: x[1])
B.sort(key=lambda x: x[0], reverse=True)
B.append([0, 0])

ANS = [0] * n
ind = n + 1
m = 0
for i in range(n):
    if B[i][1] < ind:
        ind = B[i][1]
    m += 1
    ANS[ind] += m * (B[i][0] - B[i + 1][0])

for i in ANS:
    print(i)
