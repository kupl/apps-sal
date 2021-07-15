T = int(input())
for t in range(0, T):
    N = int(input())
    count = 0
    A = []
    A = list(map(int, input().split()))
    X = N//2
    for i in range(0, N):
        if A[i] >= X:
            count += 1
    print(count)

