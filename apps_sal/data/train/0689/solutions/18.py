n = int(input())
A = []
B = []
spit = False
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for j in range(n):
    for k in range(j, n):
        if B[j] == A[k] and (B[k] + A[k] == A[j]):
            spit = True
            break
        elif (B[k] + A[k] == A[j]) and (B[j] + A[j] == A[k]):
            spit = True
            break
    if spit:
        break
if spit:
    print("YES")
else:
    print("NO")
