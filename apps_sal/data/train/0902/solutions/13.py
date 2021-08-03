t = int(input())

while t:
    t -= 1
    deeCount = 0
    dooCount = 0
    [n, starter] = input().split(' ')
    n = int(n)
    # print(n,starter)
    while n:
        n -= 1
        stack = input()
        if stack[0] == '0':
            deeCount += stack.count('0')
        else:
            dooCount += stack.count('1')
    #print(deeCount, dooCount)
    if starter == 'Dum':
        if dooCount > deeCount:
            print('Dum')
        else:
            print('Dee')
    else:
        if dooCount < deeCount:
            print('Dee')
        else:
            print('Dum')
