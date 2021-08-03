

for z in range(int(input().strip())):
    a = list(map(int, input().strip().split(' ')))
    b = a[:0:-1]
    s = 0
    k = 0
    for i in range(len(b)):
        s += b[i]
        if(s < a[0]):
            if(i == len(b) - 1):
                k += 1
            continue
        elif(s > a[0]):
            k += 1
            s = b[i]
            if(s < a[0]):
                continue
            else:
                s = 0
                k += 1
        else:
            s = 0
            k += 1
    print(k)
