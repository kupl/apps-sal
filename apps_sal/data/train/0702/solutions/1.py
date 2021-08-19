T = int(input())
for _ in range(T):
    (m, Tc, Th) = list(map(int, input().split()))
    if (Th - Tc) % 3 != 0:
        print('Yes')
    elif (Th - Tc) // 3 <= m:
        print('No')
    else:
        print('Yes')
