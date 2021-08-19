t = eval(input())
while t:
    n = eval(input())
    z = list(map(int, input().split()))
    a = [0] * 10
    for i in z:
        a[i] += 1
    if a[0] == 0:
        print(-1)
    else:
        no_1 = a[1] + a[4] + a[7]
        no_2 = a[2] + a[5] + a[8]
        s = ''
        if no_2 > no_1:
            no = (no_2 - no_1) % 3
            if no_2 == 1 and no_1 == 0:
                (a[2], a[5], a[8], a[1], a[4], a[7]) = (0, 0, 0, 0, 0, 0)
            elif no == 1:
                for k in range(2, 9, 3):
                    if a[k] != 0:
                        a[k] -= 1
                        break
            elif no == 2:
                if no_1 > 0:
                    for k in range(1, 9, 3):
                        if a[k] != 0:
                            a[k] -= 1
                            break
                else:
                    j = 2
                    i = 2
                    while j > 0:
                        if a[i] >= j:
                            a[i] -= j
                            j = 0
                        else:
                            j -= a[i]
                            a[i] = 0
                            i += 3
        elif no_2 < no_1:
            no = (no_1 - no_2) % 3
            if no_1 == 1 and no_2 == 0:
                (a[2], a[5], a[8], a[1], a[4], a[7]) = (0, 0, 0, 0, 0, 0)
            elif no == 1:
                for k in range(1, 9, 3):
                    if a[k] != 0:
                        a[k] -= 1
                        break
            elif no == 2:
                if no_2 > 0:
                    for k in range(2, 9, 3):
                        if a[k] != 0:
                            a[k] -= 1
                            break
                else:
                    j = 2
                    i = 1
                    while j > 0:
                        if a[i] >= j:
                            a[i] -= j
                            j = 0
                        else:
                            j -= a[i]
                            a[i] = 0
                            i += 3
        for i in range(9, -1, -1):
            s += str(i) * a[i]
        if len(s) == 0:
            print(-1)
        else:
            print(s)
    t -= 1
