mod=1000000007
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print(26)
    elif n==2:
        print(52)
    else:
        k=-(-n//2)
        if n%2==0:
            ans=26*(1+26*(pow(26,k-1,mod)-1)*pow(26-1,mod-2,mod))+26*(1+26*(pow(26,k-1,mod)-1)*pow(26-1,mod-2,mod))
        else:
            ans=26*(1+26*(pow(26,k-1,mod)-1)*pow(26-1,mod-2,mod))+26*(1+26*(pow(26,k-2,mod)-1)*pow(26-1,mod-2,mod))

        print(ans%mod)
