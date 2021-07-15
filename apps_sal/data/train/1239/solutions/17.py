import math
for z in range(int(input())):
    n=int(input())
    for i in range(n+1):
        print((n-i)*" ",end='')
        init=n
        for k in range(i+1):
            print(init,end='')
            init-=1
        print()
    for i in range(1,n+1):
        print(i*" ",end='')
        init=n
        for k in range(n-i+1):
            print(init,end='')
            init-=1
        print()   
