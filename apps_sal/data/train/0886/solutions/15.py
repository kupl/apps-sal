t=int(input())
for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]
    m=int(input())
    
    i=0
    j=1
    while j<n:
        arr[i],arr[j]=arr[j],arr[i]
        i=i+2
        j=j+2
    
    for i in range(n):
        arr[i]=arr[i]+arr[i]%3
    
    for i in range(n//2):
        arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
    
    l=-1
    g=10**10
    
    for i in range(n):
        if arr[i]<m:
            l=max(l,arr[i])
        if arr[i]>m:
            g=min(g,arr[i])
    
    if g==10**10:
        g=-1
    
    print(l,g)    
        
        
        

