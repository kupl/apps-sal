t = eval(input())
while t > 0:
    xx = list(map(int, input().split()))
    n = xx[0]
    m = xx[1]
    z = xx[2]
    l = xx[3]
    r = xx[4]
    b = xx[5]
    total = z + l + r + b
    maxi = n * m
    count = 0
    ar = [[0 for y in range(m)] for x in range(n)]
    truth = True
    i = 0
    while i < n:
        j = 0
        while j < m:
            ar[i][j] = 0
            if j == 0:
                if l != 0:
                    l = l - 1
                    ar[i][0] = -1
                    count = count + 1
                    if count == total:
                        truth = False
                        break
                elif b != 0:
                    b = b - 1
                    ar[i][0] = 2
                    count = count + 1
                    if count == total:
                        truth = False
                        break
                elif r != 0:
                    r = r - 1
                    ar[i][0] = 1
                    count = count + 1
                    if count == total:
                        truth = False
                        break
                elif z != 0:
                    z = z - 1
                    ar[i][0] = 0
                    count = count + 1
                    if count == total:
                        truth = False
                        break
            elif j == (m - 1):
                if ar[i][j - 1] == -1:
                    if b != 0:
                        b = b - 1
                        ar[i][j] = 2
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif l != 0:
                        l = l - 1
                        ar[i][j] = -1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                elif ar[i][j - 1] == 2:
                    if r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                elif ar[i][j - 1] == 1:
                    if r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                elif ar[i][j - 1] == 0:
                    if b != 0:
                        b = b - 1
                        ar[i][j] = 2
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif l != 0:
                        l = l - 1
                        ar[i][j] = -1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break
            else:
                if ar[i][j - 1] == -1:
                    if l != 0:
                        l = l - 1
                        ar[i][j] = -1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif b != 0:
                        b = b - 1
                        ar[i][j] = 2
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                elif ar[i][j - 1] == 2:
                    if r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                elif ar[i][j - 1] == 1:
                    if r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                elif ar[i][j - 1] == 0:
                    if l != 0:
                        l = l - 1
                        ar[i][j] = -1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif b != 0:
                        b = b - 1
                        ar[i][j] = 2
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif r != 0:
                        r = r - 1
                        ar[i][j] = 1
                        count = count + 1
                        if count == total:
                            truth = False
                            break
                    elif z != 0:
                        z = z - 1
                        ar[i][j] = 0
                        count = count + 1
                        if count == total:
                            truth = False
                            break

            if truth == False:
                break
            j = j + 1
        if truth == False:
            break
        i = i + 1
    print(count)
    t = t - 1
