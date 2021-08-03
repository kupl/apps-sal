for _ in range(int(input())):
    N, M = [int(x) for x in input().split()]
    List = []
    for i in range(N):
        Temp = [x for x in input()]
        List.append(Temp)
    Ans = 0
    for i in range(N):
        for j in range(M):
            x = 1
            while(i + x < N and j + x < M):
                if(List[i][j] == List[i][j + x] == List[i + x][j] == List[i + x][j + x]):
                    Ans += 1
                x += 1
    print(Ans)
