S = [input() for i in range(2)]
q = int(input())
ABCD = [list(map(int, input().split())) for i in range(q)]
p = [[0] for i in range(2)]
for i in range(2):
    for j, s in enumerate(S[i]):
        if s == 'A':
            p[i].append(p[i][-1] + 1)
        else:
            p[i].append(p[i][-1] + 2)
for a, b, c, d in ABCD:
    print(['NO', 'YES'][(p[0][b] - p[0][a - 1]) % 3 == (p[1][d] - p[1][c - 1]) % 3])
