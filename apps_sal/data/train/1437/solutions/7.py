def fun(l, z):
    l.sort()
    x = l[0] * l[z - 1]
    temp = []
    i = 2
    while(i * i <= x):
        if(x % i == 0):
            temp.append(i)
            if ((x // i) != i):
                temp.append(x // i)
        i += 1
    temp.sort()
    if(len(temp) != z):
        return -1
    else:
        j = 0
        for k in range(z):
            if(temp[j] != temp[k]):
                return -1
            else:
                j += 1
    return x


for i in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split(' ')))
    print(fun(arr, n))
