import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int,sys.stdin.readline().rstrip().split()))

N = I()
ans = 0
A,B = [],[]
for i in range(N):
    a,b = MI()
    A.append(a)
    B.append(b)

if A == B:
    print((0))
    return

s = sum(B)
m = s
for i in range(N):
    if A[i] > B[i]:
        m = min(m,B[i])

print((s-m))

