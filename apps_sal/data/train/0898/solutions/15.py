# cook your dish here
for i in range(int(input())):
    MN=list(map(int,input().split()))
    M=MN[0]
    N=MN[1]
    count=0
    x=0
    if N<9:
        print(count,x)
    elif N<99:
        count=M
        x=M
        print(count,x)
    elif N<999:
        count=2*M
        x=M
        print(count,M)
    elif N<9999:
        count=3*M
        x=M
        print(count,x)
    elif N<99999:
        count=4*M
        x=M
        print(count,x)
    elif N<999999:
        count=5*M
        x=M
        print(count,x)
    elif N<9999999:
        count=6*M
        x=M
        print(count,x)
    elif N<99999999:
        count=7*M
        x=M
        print(count,x)
    elif N<999999999:
        count=8*M
        x=M
        print(count,x)
    else:
        count=9*M
        x=M
        print(count,x)

