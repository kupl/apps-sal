try:
    for _ in range(int(input())):
        a,d,k,n,inc=map(int,input().split())
        p=0
        s=a
        for i in range(n//k):
            if i==0:
                s+=(k-1)*d
                d+=inc
                
            else:
                s+=k*d
                d+=inc
               
        s+=(n%k)*(d)
        print(s)
            
        
except:
    pass
