for i in range(int(input())):
    n,k = list(map(int,input().split()))  
    if n==0 and k==1 :
        print(0)
    
    elif n==0:
        print((k*(k-1))%q)
    else:
        m = n+1
        q= 10**9+7
        if k%2 ==0:
            m+=k//2-1
            print((m**2+n-m)%q)
        else:
            m+=(k+1)//2-1
            print((m**2-n-m)%q)
    

