from sys import stdin

tt = int(stdin.readline())

for loop in range(tt):

    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))

    flag = 0
    for i in range(n-1,0,-1):
        if flag == 0 and a[i-1] < a[i]:
            flag = 1
        elif flag == 1 and a[i-1] > a[i]:
            print (i)
            break
    else:
        print(0)

