try:
    t = int(input())
    for _ in range(t):
        n = int(input())
        l = []
        for y in range(1,n+1):
            l.append(y)
        if(n<4):
            print(1)
            print(n,end=" ")
            for i in range(1,n+1):
                print(i,end = " ")
            print()
        else:
            if(n%2==0):
                print(n//2)
                for i in range(1,n+1,2):
                    print(2,i,i+1)
            else:
                print(n//2)
                print(3,1,2,3)
                for i in range(4,n,2):
                    print(2,i,i+1)
except:
    pass
