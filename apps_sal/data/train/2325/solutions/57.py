S = input()
T = input()
N = int(input())
abcd = [tuple(map(int, input().split())) for _ in range(N)]

NS = len(S)
NT = len(T)
cs0 = [0] * (NS + 1)
cs1 = [0] * (NS + 1)
ct0 = [0] * (NT + 1)
ct1 = [0] * (NT + 1)
for i in range(NS):
    cs0[i + 1] = cs0[i]
    cs1[i + 1] = cs1[i]
    if S[i] == 'A':
        cs0[i + 1] += 1
    else:
        cs1[i + 1] += 1
for i in range(NT):
    ct0[i + 1] = ct0[i]
    ct1[i + 1] = ct1[i]
    if T[i] == 'A':
        ct0[i + 1] += 1
    else:
        ct1[i + 1] += 1

for a, b, c, d in abcd:
    anum = cs0[b] - cs0[a - 1]
    bnum = cs1[b] - cs1[a - 1]
    num = 0
    if anum % 3 == bnum % 3 == 0:
        num = 0
    elif anum > bnum:
        num = (anum - bnum) % 3
    else:
        num = 2 * (bnum - anum) % 3
    anum2 = ct0[d] - ct0[c - 1]
    bnum2 = ct1[d] - ct1[c - 1]
    num2 = 0
    if anum2 % 3 == bnum2 % 3 == 0:
        num2 = 0
    elif anum2 > bnum2:
        num2 = (anum2 - bnum2) % 3
    else:
        num2 = 2 * (bnum2 - anum2) % 3

    if num == num2:
        print('YES')
    else:
        print('NO')
