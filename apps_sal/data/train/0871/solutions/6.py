def find_next(arr):
    ans=[[set() for i in range(len(arr[0]))] for j in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if j>0:
                if 'R' in arr[i][j-1] and '#' not in arr[i][j]:
                    ans[i][j].add('R')
            if j<len(arr[0])-1:
                if 'L' in arr[i][j+1] and '#' not in arr[i][j]:
                    ans[i][j].add('L')
            if i>0:
                if 'D' in arr[i-1][j] and '#' not in arr[i][j]:
                    ans[i][j].add('D')
            if i<len(arr)-1:
                if 'U' in arr[i+1][j] and '#' not in arr[i][j]:
                    ans[i][j].add('U')
            if '#' in arr[i][j]:
                ans[i][j].add("#")
    return ans

def cal(arr):
    ans=0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            n=len(arr[i][j])
            ans+=n*(n-1)//2
    return ans
t=int(input())
for _ in range(t):
    r,c=list(map(int,input().split()))
    arr=[]
    for i in range(r):
        toadd=list(map(set,list(input())))
        arr+=[toadd]
    ans=0
    for i in range(max(r,c)):
        arr=find_next(arr)
        ans+=cal(arr)
    print(ans)
        

