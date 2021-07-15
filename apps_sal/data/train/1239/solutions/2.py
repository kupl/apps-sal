for _ in range(int(input())):
    n=int(input())
    for i in range(n+1):
        k=n
        for j in range(1,n-i+1):
            print(' ',end='')
        for j in range(i+1):
            print(k,end='')
            k-=1
        print()
    for i in range(n-1,-1,-1):
        k=n
        for j in range(1,n-i+1):
            print(' ',end='')
        for j in range(i+1):
            print(k,end='')
            k-=1
        print()
