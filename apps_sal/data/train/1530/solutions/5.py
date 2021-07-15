for i in range(int(input())):
    p=int(input())
    k=1
    print(1,end="")
    print()
    s=0
    for i in range(1,p):
        k+=i+1
        x=k
        for j in range(i+1):
            print(x,end="")
            x-=1
        print()
        
