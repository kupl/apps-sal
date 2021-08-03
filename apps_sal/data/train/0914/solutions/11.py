T = int(input())
while(T > 0):
    N, M = [int(x) for x in input().split()]
    arr = [[int(x) for x in input().split()] for y in range(N)]
    ans = [['1' for x in range(M)] for y in range(N)]
    for i in range(1, N):
        for j in range(M):
            m = max(arr[i][j], arr[i - 1][j])
            if(j - 1 >= 0):
                m = max(m, arr[i - 1][j - 1])
            if(j + 1 < M):
                m = max(m, arr[i - 1][j + 1])
            if(arr[i][j] != m):
                ans[i][j] = '0'
            arr[i][j] = m
    for i in range(N):
        print(''.join(ans[i]))
    T -= 1
