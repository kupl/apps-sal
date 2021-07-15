for _ in range(int(input())):
    n=int(input())
    for i in range(0,n):
        for j in range(0,n):
            if i==n-1 or j==0 or i==j:
                print('*',end='')
            else:
                print(end=' ')
        print()
