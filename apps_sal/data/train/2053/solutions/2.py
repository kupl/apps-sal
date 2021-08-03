N, M = list(map(int, input().split()))
A = sorted([int(a) for a in input().split()])[::-1]
B = sorted([int(a) for a in input().split()])
if A[0] > B[0]:
    print(-1)
else:
    ans = 0
    for a in A:
        ans += a * M

    i = 0
    j = M - 1
    for b in B:
        if b > A[0]:
            ans += b - A[i]
            j -= 1
            if j == 0:
                i += 1
                j = M - 1
    print(ans)
