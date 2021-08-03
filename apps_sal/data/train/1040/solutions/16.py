

T = int(input())
for test in range(T):
    N, Q = [int(v) for v in input().split()]
    S = input()
    start_points = [len(set(S[i:i + 3])) < 3 for i in range(N - 2)]
    if N < 3:
        count = []
    else:
        counts = [int(start_points[0])] + [0] * (N - 3)
        for i in range(1, N - 2):
            counts[i] = counts[i - 1] + start_points[i]
    # print("counts = "+str(counts))
    for query in range(Q):
        L, R = [int(v) for v in input().split()]
        if L + 2 > R:
            print("NO")
            continue
        if L == 1:
            left = 0
        else:
            left = counts[L - 2]
        right = counts[R - 3]
        # print("query = "+str((L,R))+" left, right = "+str((left,right)))
        if left < right:
            print("YES")
        else:
            print("NO")
