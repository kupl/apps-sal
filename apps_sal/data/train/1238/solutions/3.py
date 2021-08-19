test = int(input())
for i in range(test):
    N = input()
    X = []
    for x in N:
        X.append(x)
    Y = []
    list1 = []
    output = ''
    for y in X:
        if int(y) >= 6 and int(y) not in Y:
            Y.append(y)
    for x in Y:
        for y in X:
            if int(x) == 6:
                if int(y) >= 5:
                    n = int(x) * 10 + int(y)
                    list1.append(n)
            else:
                n = int(x) * 10 + int(y)
                list1.append(n)
    for j in Y:
        m = int(j) * 10 + int(j)
        list1.remove(m)
    list1.sort()
    if len(list1) == 0:
        print(' ')
    else:
        list1.sort()
        for k in list1:
            if chr(k) not in output and k < 91:
                output += chr(k)
        print(output)
