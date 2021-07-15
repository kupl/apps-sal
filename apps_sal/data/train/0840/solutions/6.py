# cook your dish here
for _ in range(int(input())):
    n = int(input())
    for i in range(n//2 +1):
        for j in range(i):
            print(' ',end = '')
        print('*')
    for i in range(n//2 -1,0,-1):
        for j in range(i):
            print(' ',end = '')
        print('*')
    if(n>1):
        print('*')
