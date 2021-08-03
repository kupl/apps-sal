t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]

    a = [x for x in input().split()]
    a.reverse()

    flag = 0
    for i in range(k):
        if(flag == 0 and a[i] == 'H'):
            flag = 1
        elif(flag == 1 and a[i] == 'T'):
            flag = 0

    a = a[k:]
    if(flag == 0):
        print(a.count('H'))
    else:
        print(a.count('T'))
