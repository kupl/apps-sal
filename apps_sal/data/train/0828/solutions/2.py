# cook your dish here
for t in range(int(input())):
    total=0
    n=int(input())
    a=list(map(int,input().split()))
    
    for i in range(0,n):
        
        if a[i]==0:
            total=total+1100
        else:
            if total>=1100:
                
                total=total-1000
                total=total+1100
    print(total)
        
    
    
    
