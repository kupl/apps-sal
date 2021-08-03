N = int(input())
A = [int(i) for i in input().split()]
C = []
l = 0
C.append(([(0, -1), (A[0], 0)]))
for i in range(1, 2**N):
    biggest, second = (A[i], i), (0, -1)
    for k in range(l + 1):
        if i & (1 << k):
            for a in C[i ^ (1 << k)]:
                if a[0] > biggest[0]:
                    second = biggest
                    biggest = a
                elif a[0] > second[0] and biggest != a:
                    second = a
    C.append([second, biggest])
    if i == 2**(l + 1) - 1:
        l += 1
ans = [0]
for i in range(1, 2**N):
    a, b = C[i]
    ans.append(max(ans[-1], a[0] + b[0]))
    print(ans[-1])
