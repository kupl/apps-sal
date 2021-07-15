S = input().rstrip()
T = input().rstrip()
AS = [0]
AT = [0]
for s in S:
    if s=="A": AS.append(AS[-1]+1)
    else: AS.append(AS[-1]+2)
for s in T:
    if s=="A": AT.append(AT[-1]+1)
    else: AT.append(AT[-1]+2)
Q = int(input())
for _ in range(Q):
    a, b, c, d = map(int, input().split())
    if (AS[b]-AS[a-1])%3 == (AT[d]-AT[c-1])%3: print("YES")
    else: print("NO")
