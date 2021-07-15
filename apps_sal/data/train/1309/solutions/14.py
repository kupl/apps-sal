for _ in range(int(input())):
    n=int(input())
    for _ in range(n,0,-1):
        x=_
        print('*'*(n-_),end="")
        for _ in range(x):
            print(x-_,end="")
        print()    
        
