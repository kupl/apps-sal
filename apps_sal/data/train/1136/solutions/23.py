# cook your dish here
t=int(input())

while t:
    t-=1
    
    n,k= list(map(int,input().split()))
    
    
    if n%2==0:
        
        print((n//2)*k)
    else:
        print(((n//2)+1)*k)

