ans = 0
for _ in range(int(input())):
    n = int(input())
    A, B, C, D = [0] * 4, [0] * 4, [0] * 4, [0] * 4
    for i in range(n):
        m, t = map(str, input().split())
        if m == 'A':
            if t == '12':
                A[0] += 1
            elif t == '3':
                A[1] += 1
            elif t == '6':
                A[2] += 1
            else:
                A[3] += 1
        elif m == 'B':
            if t == '12':
                B[0] += 1
            elif t == '3':
                B[1] += 1
            elif t == '6':
                B[2] += 1
            else:
                B[3] += 1
        elif m == 'C':
            if t == '12':
                C[0] += 1
            elif t == '3':
                C[1] += 1
            elif t == '6':
                C[2] += 1
            else:
                C[3] += 1
        else:
            if t == '12':
                D[0] += 1
            elif t == '3':
                D[1] += 1
            elif t == '6':
                D[2] += 1
            else:
                D[3] += 1
    ans1 = -400
    for i in range(4):
        for j in range(4):
            if j == i:
                continue
            for k in range(4):
                if k == i or k == j:
                    continue
                for l in range(4):
                    if l == i or l == j or l == k:
                        continue
                    din = [A[i], B[j], C[k], D[l]]
                    din.sort(reverse=True)
                    count = (100 * din[0]) + (75 * din[1]) + (50 * din[2]) + (25 * din[3])
                    count -= (100 * (din.count(0)))
                    if count > ans1:
                        ans1 = count
    print(ans1)
    ans += ans1
print(ans)
