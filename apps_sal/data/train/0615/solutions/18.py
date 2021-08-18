T = int(input())
for i in range(T):
    N, Q = map(int, input().split())
    lis = list(map(int, input().split()))
    cumSum = [0]
    for j in lis:
        cumSum.append(cumSum[-1] + j)
    for j in range(Q):
        x, y = map(int, input().split())
        print(cumSum[y] - cumSum[x - 1])
