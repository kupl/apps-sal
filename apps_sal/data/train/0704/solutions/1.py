for _ in range(int(input())):
    a,n,m = map(int,input().split(' '))
    print((((pow(10,n*(len(str(a))),(10**(len(str(a))) - 1)*m)-1)//(10**(len(str(a))) - 1))%m)*(a%m)%m)
