import numpy as np
for t in range(int(input())):
    n = list(input())
    arr = [int(x) for x in n]
    num = []
    if 6 in arr:
        for i in arr:
            if i >= 5:
                num.append(6 * 10 + i)
    if 66 in num:
        num.remove(66)
    if 7 in arr:
        for i in arr:
            num.append(7 * 10 + i)
    if 77 in num:
        num.remove(77)
    if 8 in arr:
        for i in arr:
            num.append(8 * 10 + i)
    if 88 in num:
        num.remove(88)
    if 9 in arr:
        if 0 in arr:
            num.append(90)
    num = np.array(num)
    np.sort(num)
    ch = ''
    for i in np.unique(num):
        ch += chr(i)
    print(ch)
