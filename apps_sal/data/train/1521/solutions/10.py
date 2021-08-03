for _ in range(int(input())):
    N = int(input())
    start = []
    end = []
    for i in range(N):
        a, b = list(map(int, input().split()))
        start.append([a, i])
        end.append([b, i])
    start.sort()
    end.sort()
    scores = [0] * N
    for i in range(N):
        p = start[i]
        q = end[i]
        scores[p[1]] += (N - i - 1)
        scores[q[1]] += i
    print(*scores)
