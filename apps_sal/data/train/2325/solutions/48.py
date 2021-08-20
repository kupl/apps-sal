from itertools import accumulate
S = input()
T = input()
q = int(input())
abcds = [tuple(map(int, input().split())) for _ in range(q)]
S_csum = list(map(lambda x: x % 3, accumulate(map(lambda c: 1 if c == 'A' else -1, S), initial=0)))
T_csum = list(map(lambda x: x % 3, accumulate(map(lambda c: 1 if c == 'A' else -1, T), initial=0)))
for (a, b, c, d) in abcds:
    if (S_csum[b] - S_csum[a - 1]) % 3 == (T_csum[d] - T_csum[c - 1]) % 3:
        print('YES')
    else:
        print('NO')
