t = int(input())


def getBin(x):
    return x >= 0 and str(bin(x))[2:] or '-' + str(bin(x))[3:]


while t:
    n = int(input())
    if n % 2 == 0:
        print(0)
    else:
        lst = []
        arr = getBin(n)
        for i in range(0, len(arr) - 1):
            if arr[i] == '1':
                lst.append('2')
            if arr[i] == '0':
                lst.append('1')
        print(''.join(lst))
    t = t - 1
