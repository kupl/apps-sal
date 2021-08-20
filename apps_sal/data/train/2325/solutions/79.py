S = [0] + [1 if a == 'A' else 2 for a in input()]
T = [0] + [1 if a == 'A' else 2 for a in input()]
for i in range(1, len(S)):
    S[i] += S[i - 1]
for i in range(1, len(T)):
    T[i] += T[i - 1]
for _ in range(int(input())):
    (a, b, c, d) = list(map(int, input().split()))
    if (S[b] - S[a - 1] - T[d] + T[c - 1]) % 3 == 0:
        print('YES')
    else:
        print('NO')
