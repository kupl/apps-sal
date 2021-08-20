Q = int(input())
querys = [tuple(map(int, input().split())) for _ in range(Q)]
anss = []
for (A, B) in querys:
    if A > B:
        (A, B) = (B, A)
    if A == B:
        ans = 2 * (A - 1)
    elif A + 1 == B:
        ans = 2 * (A - 1)
    else:
        C = -(-(A * B) ** 0.5 // 1) - 1
        if C * (C + 1) >= A * B:
            ans = 2 * (C - 1)
        else:
            ans = 2 * C - 1
    anss.append(int(ans))
print('\n'.join(map(str, anss)))
