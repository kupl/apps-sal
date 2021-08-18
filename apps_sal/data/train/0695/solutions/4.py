t = int(input())
for i in range(t):
    x, y, n = [int(i) for i in input().split()]

    bx = list(bin(x))
    by = list(bin(y))
    bx.remove(bx[0])
    bx.remove(bx[0])
    by.remove(by[0])
    by.remove(by[0])
    lx = len(bx)
    ly = len(by)
    index = 0
    flag = 2
    k = -1
    if(lx != ly):
        index = max(lx, ly)
        if((n + 1) % 2**(index) >= 2**(index - 1)):
            k = 2**(index - 1)
        else:
            k = (n + 1) % (2**(index))

        if(lx < ly):
            print(int((n + 1) / 2**index) * (2**(index - 1)) + k)
        else:
            print(n + 1 - (int((n + 1) / 2**index) * (2**(index - 1)) + k))

    else:

        for j in range(lx):
            if(bx[j] != by[j]):
                index = lx - j
                if(bx[j] == '0'):
                    flag = 0
                else:
                    flag = 1
                break
        if((n + 1) % 2**(index) >= 2**(index - 1)):
            k = 2**(index - 1)
        else:
            k = (n + 1) % (2**(index))
        if(flag == 2):
            print(0)
        elif(flag == 1):
            print(n + 1 - (int((n + 1) / 2**index) * (2**(index - 1)) + k))
        else:
            print(int((n + 1) / 2**index) * (2**(index - 1)) + k)
