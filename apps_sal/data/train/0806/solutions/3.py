t = int(input())
for i in range(t):
    n = int(input())
    q0 = n
    (a, b, c) = list(map(int, input().split()))
    list1 = [n]
    k = 1
    while len(list1) - list1.index(n) - 1 < 3 or (len(list1) - 1 - list1.index(n)) % 3 != 0:
        if k == 1:
            n /= a
            k = 2
        elif k == 2:
            n /= b
            k = 3
        elif k == 3:
            n /= c
            k = 1
        fd = str(n)[0]
        if int(n * 10) % 10 != 0:
            list1.append(int(n * 10) % 10)
        else:
            list1.append(int(fd))
        n = list1[-1]
    del list1[-1]
    list2 = list1[list1.index(n):]
    for j in range(int(input())):
        q = int(input())
        if q < len(list1):
            print(list1[q])
        else:
            print(list2[(q - list1.index(n)) % len(list2)])
