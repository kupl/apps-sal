S = input()
SA = [0]
n = 0
for c in S:
    if c=='A': n+=1
    SA.append(n)

T = input()
TA = [0]
n = 0
for c in T:
    if c=='A': n+=1
    TA.append(n)


q = int(input())
for _ in range(q):
    a, b, c, d = list(map(int, input().split()))

    nSA = SA[b]-SA[a-1]
    nSB = b-a+1-nSA
    nTA = TA[d]-TA[c-1]
    nTB = d-c+1-nTA

    print(('YES' if (nSA-nSB)%3 == (nTA-nTB)%3 else 'NO'))

