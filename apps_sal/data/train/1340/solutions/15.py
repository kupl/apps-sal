try:
    import sys
    from sys import stdin
    import math

    def iinput():
        return int(input())

    def minput():
        return map(int, input().split())

    def linput():
        return list(map(int, input().split()))

    def fiinput():
        return int(stdin.readline())

    def fminput():
        return map(int, stdin.readline().strip().split())

    def flinput():
        return list(map(int, stdin.readline().strip().split()))

    for _ in range(iinput()):
        n = iinput()
        list1 = linput()
        c = 0
        s = 0
        for i in range(n):
            if(list1[i] > 0):
                c += 1
                s += list1[i]
        list2 = []
        for i in range(c):
            if(list1[i] <= 0):
                list2.append(i + 1)
        for i in range(c, n):
            if(list1[i] > 0):
                list2.append(i + 1)
        print(s)
        print(len(list2), *list2)

except:
    pass
