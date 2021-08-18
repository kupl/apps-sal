import sys
input = sys.stdin.readline

n, q = list(map(int, input().split()))
A = list(map(int, input().split()))

if max(A) == min(A):
    print(0)
    return


L = max(A)

MM = [[200005, -1, i] for i in range(L + 1)]
COUNT = [0] * (L + 1)

for i in range(n):
    a = A[i]
    MM[a][0] = min(MM[a][0], i)
    MM[a][1] = max(MM[a][1], i)
    COUNT[a] += 1

MM.sort()

i, j, k = MM[0]

MAX = j
CC = COUNT[k]
MAXC = COUNT[k]
ANS = 0

for i, j, k in MM[1:]:
    if i == 200005:
        ANS += CC - MAXC
        break

    if MAX < i:
        ANS += CC - MAXC

        MAX = j
        CC = COUNT[k]
        MAXC = COUNT[k]

    else:
        CC += COUNT[k]
        MAX = max(MAX, j)
        MAXC = max(MAXC, COUNT[k])

print(ANS)
