for _ in range(int(input())):
    M,N=list(map(int,input().split()))
    length=len(str(N))
    initial="9"
    initial=initial*(length)
    factor=0
    if int(initial)>N:
        factor=length-1
    else:
        factor=length
    if factor==0:
        M=0
    print(factor*M,M)


