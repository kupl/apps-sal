from bisect import bisect_left, bisect_right
(N, Q) = map(int, input().split())
STX = [[int(i) for i in input().split()] for _ in range(N)]
D = [int(input()) for _ in range(Q)]
STX.sort(key=lambda x: x[2])
ans = [-1] * Q
skip = [-1] * Q
for (S, T, X) in STX:
    left = bisect_left(D, S - X)
    right = bisect_right(D, T - X - 1)
    while left < right:
        if skip[left] < 0:
            skip[left] = right
            ans[left] = X
            left += 1
        else:
            left = skip[left]
print(*ans, sep='\n')
