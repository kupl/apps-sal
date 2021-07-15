mod=10**9+7
inv=pow(25,mod-2,mod)
for i in range(int(input())):
    N=int(input())
    if(N%2==0):
        r=((2*26*(pow(26,N//2,mod)-1))%mod*inv)%mod
    else:
        r=((27*pow(26,N//2+1,mod)-52)%mod*inv)%mod
    print(r)

