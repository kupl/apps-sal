for _ in range(int(input())):
    n,k=[int(x) for x in input().split()]
    if k%4==0:
        for i in range(0,k,4):
            print(i,i+1)
            print(i+1,i+2)
            print(i+2,i+3)
            print(i+3,i)
    elif k%4==1:
        for i in range(4,k-1,4):
            print(i,i+1)
            print(i+1,i+2)
            print(i+2,i+3)
            print(i+3,i)
        print(0,1)
        print(1,2)
        print(2,3)
        print(3,(1<<n)-1)
        print((1<<n)-1,0)
    elif k%4==2:
        for i in range(4,k-2,4):
            print(i,i+1)
            print(i+1,i+2)
            print(i+2,i+3)
            print(i+3,i)
        print(0,1)
        print(1,2)
        print(2,3)
        print(3,(1<<n)-2)
        print((1<<n)-2,(1<<n)-1)
        print((1<<n)-1,0)
    elif k!=3:
        n=1<<n
        n-=1
        for i in range(4,k-3,4):
            print(i,i+1)
            print(i+1,i+2)
            print(i+2,i+3)
            print(i+3,i)
        print(2,3)
        print(3,n-1)
        print(n-1,0)
        print(0,1)
        print(1,n-2)
        print(n-2,n)
        print(n,2)
    else:
        print(0,1)
        print(1,3)
        print(3,0)

