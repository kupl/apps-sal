for _ in range(int(input())):
    n=int(input())
    for i in range(0,n+1):
        for j in range(0,i+1):
            if i==j:
                print(j,end='')
            else:
                print('*',end='')
        print()
