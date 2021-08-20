try:
    import math
    from collections import defaultdict
    from sys import stdin
    for _ in range(int(stdin.readline())):
        (n, x) = list(map(int, stdin.readline().strip().split()))
        list1 = list(map(int, stdin.readline().strip().split()))
        ll = set()
        for i in range(1, n):
            list1[i] = list1[i] + list1[i - 1]
        c = 0
        for i in range(1, n + 1):
            if x % i == 0:
                a = i
                y = x // a
                list2 = [0] * (y + 1)
                j = -1
                dict1 = {}
                for i in range(a - 1, n):
                    if j == -1:
                        if list1[i] <= y:
                            list2[list1[i]] += 1
                        j += 1
                    else:
                        if list1[i] - list1[j] <= y:
                            list2[list1[i] - list1[j]] += 1
                        j += 1
                j = -1
                for i in range(a - 1, n):
                    if j == -1:
                        if list1[i] <= y:
                            c += list2[y - list1[i]]
                        j += 1
                    else:
                        if list1[i] - list1[j] <= y:
                            if list1[i] - list1[j] <= y:
                                c += list2[y - (list1[i] - list1[j])]
                        j += 1
        print(c)
except:
    pass
