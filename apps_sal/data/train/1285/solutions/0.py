T = int(input())
for k in range(0, T):
    N = int(input())
    matrix = []
    for i in range(0, N):
        a = list(map(int, input().split()))
        matrix.append(a)
    max_trace = []
    for i in range(0, N):
        trace1 = 0
        trace2 = 0
        for j in range(0, i + 1):
            trace1 += matrix[j][N + j - i - 1]
            trace2 += matrix[N + j - i - 1][j]
            max_trace.append(trace1)
            max_trace.append(trace2)
    print(max(max_trace))
