S = input()
T = input()

accSA = [0] * (len(S) + 1)
accSB = [0] * (len(S) + 1)

for i, s in enumerate(S):
    accSA[i + 1] += accSA[i]
    accSB[i + 1] += accSB[i]
    if s == 'A':
        accSA[i + 1] += 1
    else:
        accSB[i + 1] += 1

accTA = [0] * (len(T) + 1)
accTB = [0] * (len(T) + 1)

for i, s in enumerate(T):
    accTA[i + 1] += accTA[i]
    accTB[i + 1] += accTB[i]
    if s == 'A':
        accTA[i + 1] += 1
    else:
        accTB[i + 1] += 1

Q = int(input())
ans = []
for _ in range(Q):
    a, b, c, d = map(int, input().split())

    sA = accSA[b] - accSA[a - 1]
    sB = accSB[b] - accSB[a - 1]
    tA = accTA[d] - accTA[c - 1]
    tB = accTB[d] - accTB[c - 1]

    sA = (sA + sB * 2) % 3
    tA = (tA + tB * 2) % 3

    ans.append('YES' if sA == tA else 'NO')
print(*ans, sep='\n')
