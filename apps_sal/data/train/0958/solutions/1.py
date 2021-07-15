for _ in range(int(input())):
    n=int(input())
    if n==1:
        print('*')
        print()
        continue
    for i in range(n-1):
        if i==0:
            for j in range(2*n-1):
                if j==n-1:
                    print('*',end='')
                else:
                    print(end=' ')
            print()
            print()
            continue
        for j in range(2*n-1):
            if(j==n-1-i or j==n-1+i):
                print('*',end='')
            else:
                print(end=' ')
        print()
        print()
    for j in range(2*n-1):
        print('*',end='')
    print()
    print()
