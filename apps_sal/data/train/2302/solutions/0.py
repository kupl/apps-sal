n, d = list(map(int, input().split()))
D = list(map(int, input().split()))
A = [0]*(n+1)
P = [0]*(n+1)

P[0] = pos = d
for i, x in enumerate(D):
    if x <= 2*pos:
        pos = abs(x-pos)
    P[i+1] = pos
    if pos == 0:
        break

for i in range(n-1, -1, -1):
    if D[i] <= 2*A[i+1]+1:
        A[i] = A[i+1] + D[i]
    else:
        A[i] = A[i+1]

q = input()
Q = list(map(int, input().split()))
for i in Q:
    if P[i-1] <= A[i] and pos == 0:
        print("NO")
    else:
        print("YES")

