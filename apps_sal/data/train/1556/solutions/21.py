# cook your dish here


for _ in range(int(input())):
    n=int(input())
    # c=1
    for i in range(0,n):
        for j in range(0,n):
            if (j)%2==0:
                print('1',end='')
            else:
                print('0',end="")
            # print(i+j,end="")
            # c+=2
        print()
