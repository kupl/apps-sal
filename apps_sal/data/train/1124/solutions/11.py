t = int(input())
while t > 0:
    (n, p, q) = input().split(' ')
    n = int(n)
    p = int(p)
    q = int(q)
    l = list(map(int, input().split(' ')))
    if q == 0:
        s = 0
        count = 0
        l.sort()
        for i in l:
            s = s + i
            if s > p:
                break
            else:
                count = count + 1
        print(count)
    elif p == 0:
        l1 = list(filter(lambda x: x % 2 == 0, l))
        s = 0
        count = 0
        l1.sort()
        for i in l1:
            s = s + i
            if s > 2 * q:
                break
            else:
                count = count + 1
        print(count)
    else:
        count = 0
        s = 0
        sum = p + 2 * q
        l1 = list(filter(lambda x: x % 2, l))
        l2 = list(filter(lambda x: x % 2 == 0, l))
        l1.sort()
        l2.sort()
        if len(l1) <= len(l2):
            x = len(l1)
        else:
            x = len(l2)
        i = 0
        j = 0
        lst = []
        while i + j < len(l1) + len(l2) - 1:
            if i == len(l1):
                lst.append(l2[j])
                j = j + 1
            if j == len(l2):
                lst.append(l1[i])
                i = i + 1
            if l1[i] < l2[j]:
                if p > 0:
                    lst.append(l1[i])
                    p = p - 1
                    i = i + 1
                else:
                    i = i + 1
            else:
                lst.append(l2[j])
                j = j + 1
        for i in lst:
            s = s + i
            if s > sum:
                break
            else:
                count = count + 1
        print(count)
    t = t - 1
