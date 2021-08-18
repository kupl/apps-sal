N = int(input())
A = list(map(int, input().split()))

A = [[a, 0] for a in A]
step = 1
for _ in range(N):
    step *= 2
    for s in range(2**N):
        if (s // (step // 2)) % 2 == 0:
            continue
        tmp = A[s] + A[s - step // 2]
        tmp.sort()
        A[s] = [tmp[-1], tmp[-2]]
tmp = 0
for s in range(1, 2**N):
    tmp = max(tmp, sum(A[s]))
    print(tmp)
