for _ in range(int(input())):
    n,s=input().split()
    n=int(n)
    l=len(s)
    m=1000000007

    if n>l:        
     ans=(pow(26,n-l-1,m))
     ans*=(26+25*l)
     print(ans%m)

    else:
     print("0")

