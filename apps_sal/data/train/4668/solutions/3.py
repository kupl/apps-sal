def is_divisible_by_6(s):
    if s[-1] != '*':
        if int(s[-1]) % 2 == 1:
            return []
        else:
            lst = []
            for i in range(10):
                if int(s.replace('*', str(i))) % 3 == 0:
                    lst.append(int(s.replace('*', str(i))))
            for x in range(len(lst)):
                lst[x] = str(lst[x])
            return lst
    else:
        lst = []
        for i in [0, 2, 4, 6, 8]:
            lst.append(s[:-1] + str(i))
        lst2 = []
        for x in range(len(lst)):
            if int(lst[x]) % 3 == 0:
                lst2.append(lst[x])
        return lst2
