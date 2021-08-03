# AB -> BBAA -> BAAAA -> BA
# Thus, this problem has commutative property.
# So, if we let A and B satisfy x^2 + x + 1 == 0,
# then A^2 == B, B^2 == A, and A^3 == B^3 == 1.
# So this makes an invariant.

from itertools import accumulate

S = input()
T = input()
q = int(input())
abcds = [tuple(map(int, input().split())) for _ in range(q)]

S_csum = list(map(lambda x: x % 3, [0] + list(accumulate(map(lambda c: 1 if c == 'A' else -1, S)))))
T_csum = list(map(lambda x: x % 3, [0] + list(accumulate(map(lambda c: 1 if c == 'A' else -1, T)))))

for a, b, c, d in abcds:
    if (S_csum[b] - S_csum[a - 1]) % 3 == (T_csum[d] - T_csum[c - 1]) % 3:
        print("YES")
    else:
        print("NO")
