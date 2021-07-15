# cook your dish here
for _ in range(int(input())):
    n=int(input())
    # c=1
    for i in range(0,n):
        for j in range(0,n):
            if (i+j)%2==0:
                print('0',end='')
            else:
                print('1',end="")
            # print(i+j,end="")
            # c+=2
        print()
