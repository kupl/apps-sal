t = int(input())
listd = []
listr = []
while t:
    n = int(input())
    x = n
    while n:
        (a, b) = input().split(' on ')
        listd.append(a)
        listr.append(b)
        n = n - 1
    print('Begin on ' + listr.pop())
    listd.pop(0)
    x = x - 1
    while x:
        temp = listd.pop()
        if temp == 'Left':
            print('Right on ' + listr.pop())
        else:
            print('Left on ' + listr.pop())
        x = x - 1
    print('')
    t = t - 1
