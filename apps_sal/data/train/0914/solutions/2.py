# cook your dish here
for _ in range(int(input())):
    N,M=list(map(int,input().split()))
    matrix=[]
    for i in range(N):
        l=list(map(int,input().split()))
        matrix.append(l)
    for i in range(1,N):
        for j in range(M):
            if(j==0):
                if(max(matrix[i-1][j],matrix[i-1][j+1])>matrix[i][j]):
                    matrix[i][j]=max(matrix[i-1][j],matrix[i-1][j+1])
            elif(j==M-1):
                if(max(matrix[i-1][j],matrix[i-1][j-1])>matrix[i][j]):
                    matrix[i][j]=max(matrix[i-1][j],matrix[i-1][j-1])
            else:
                if(max(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])>matrix[i][j]):
                    matrix[i][j]=max(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])
    # print(matrix)
    ans=[[1]*M for i in range(N)]
    for i in range(1,N):
        for j in range(M):
            if(j==0):
                if(max(matrix[i-1][j],matrix[i-1][j+1])>=matrix[i][j]):
                    ans[i][j]=0
            elif(j==M-1):
                if(max(matrix[i-1][j],matrix[i-1][j-1])>=matrix[i][j]):
                    ans[i][j]=0
            else:
                if(max(matrix[i-1][j-1],matrix[i-1][j],matrix[i-1][j+1])>=matrix[i][j]):
                    ans[i][j]=0
    for i in range(N):
        for j in range(M):
            print(ans[i][j],end="")
        print()
                
