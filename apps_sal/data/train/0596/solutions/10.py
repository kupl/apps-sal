# cook your dish here
try:
    t=int(input())
    for _ in range(t):
        a,b=map(int,input().split())
        if(a==0):
            print(((b-1)*b)%1000000007)
        else:
            inc=b%2
            if(inc==0):
                cir=(b-2)//2
                ans=(a+cir)*(a+cir+1)+a
                print(ans%1000000007)
            else:
                cir=b//2
                ans=(a+cir-1)*(a+cir)
                ans=(ans+a+2*cir)
                print(ans%1000000007)
except:
    pass
