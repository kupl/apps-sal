t = str.maketrans('0123456789', '0101010101')
C = (1 << 18) * [0]
for _ in range(int(input())):
    (c, a) = input().split()
    if '?' == c:
        print(C[int(a, 2)])
    else:
        C[int(a.translate(t), 2)] += 1 if '-' != c else -1
