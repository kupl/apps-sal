tc = int(input())
for _ in range(tc):
    (N, M) = map(int, input().split())
    arr = list(map(int, input().split()))
    curr_mex = 1
    arr.sort()
    for i in range(N):
        if arr[i] == curr_mex:
            curr_mex += 1
    if curr_mex == M:
        print(N)
    elif curr_mex < M:
        print(-1)
    else:
        cnt = 0
        for x in arr:
            if x == M:
                cnt += 1
        print(N - cnt)
