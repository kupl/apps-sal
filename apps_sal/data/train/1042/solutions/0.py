# cook your dish here
    
def G(x, y): 
   while(y): 
       x, y = y, x % y 
   return x 
# t=int(input())
# l=list(map(int,input().split()))
for _ in range(int(input())):
    n,p=map(int,input().split())

    c=0
    for i in range(1,n+1):
        if G(i,p)==1:
            c+=1
    ans=c*(c-1)//2
    print(ans)
