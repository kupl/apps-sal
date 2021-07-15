#code
#code
t=int(input())
for i in range(t):
    #n,k=list(map(int,input().split()))
    arr=[]
    n,m=map(int,input().split())
    z=['1' for i in range(m)]
    arr.append(list(map(int,input().split())))
    print("".join(z))
    for i in range(1,n):
        x=''
        arr.append(list(map(int,input().split())))
        if arr[i][0]>arr[i-1][0] and arr[i][0]>arr[i-1][1]:
            x+='1'
        else:
            x+='0'
        arr[i][0]=max(arr[i-1][0],arr[i][0],arr[i-1][1])
        for j in range(1,m-1):
            if arr[i][j]>arr[i-1][j] and arr[i][j]>arr[i-1][j+1] and arr[i][j]>arr[i-1][j-1]:
                x+='1'
            else:
                x+='0'
            arr[i][j]=max(arr[i-1][j],arr[i][j],arr[i-1][j+1],arr[i-1][j-1])
        if arr[i][m-1]>arr[i-1][m-1] and arr[i][m-1]>arr[i-1][m-2]:
            x+='1'
        else:
            x+='0'
        arr[i][m-1]=max(arr[i-1][m-2],arr[i][m-1],arr[i-1][m-1])
        print(x)
        
