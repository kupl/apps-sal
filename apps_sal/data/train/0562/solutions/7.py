import sys

dp=[[0 for i in range(201)]for i in range(201)]
Q =[sys.maxsize for i in range(201)]
Q1=[sys.maxsize for i in range(201)]


def compareWith(A ,B ,n ,m , f):
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            
            a=0
            if(A[i-1][j-1]!=B[i-1][j-1]):
                a=1
            
            dp[i][j]=a + dp[i-1][j] + dp[i][j-1] -dp[i-1][j-1]
            
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            k=i
            l=j
            r=1
            while k<=n and l<=m:
                a=findError(i,j,k,l)
                Q[r]=min(Q[r],a)
                k+=1
                l+=1
                r+=1
                
    if f==1:
        Q1=Q[:]


def findError(i,j,k,l):
    return dp[k][l]-dp[k][j-1]-dp[i-1][l]+dp[i-1][j-1]
    



n, m = map(int, input().split()) 

A=[]
C=[]
B=[]

for i in range(n):
    s=input()
    A.append(s)
    
for i in range(n):
    sb=""
    sc=""
    for j in range(m):
        if(i%2==0):
            if(j%2==0):
                sb+='1'
                sc+='0'
            else:
                sb+='0'
                sc+='1'
        else:
            if(j%2==1):
                sb+='1'
                sc+='0'
            else:
                sb+='0'
                sc+='1'
    B.append(sb)
    C.append(sc)
    
# print(*B, sep='\n')
# print("****")
# print(*C, sep='\n')

compareWith(A,B,n,m,1)
compareWith(A,C,n,m,0)

q=int(input())
c=list(map(int,input().split()))

for i in c:
    a=0
    for j in range(1,min(m,n)+1):
        if i>=Q[j] or i>=Q1[j]:
            a=max(a,j)
    
    print(a)


    
