for _ in range(int(input())):
    n = int(input())
    (s1, s2) = (input(), input())
    (a1, a2) = ([0] * 26, [0] * 26)
    for v in map(ord, s1):
        a1[v - 97] += 1
    for v in map(ord, s2):
        a2[v - 97] += 1
    if a1 != a2:
        print('NO')
        continue
    if max(a1) > 1:
        print('YES')
        continue
    inv1 = sum((c1 > c2 for (i, c1) in enumerate(s1) for c2 in s1[i + 1:]))
    inv2 = sum((c1 > c2 for (i, c1) in enumerate(s2) for c2 in s2[i + 1:]))
    print('YES' if inv1 % 2 == inv2 % 2 else 'NO')
