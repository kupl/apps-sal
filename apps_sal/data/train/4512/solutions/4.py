from itertools import count


def find_num(n):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 11, 20]
    while len(a) <= n:
        for i in count(11):
            if i in a:
                continue
            if not set(str(i)) & set(str(a[-1])):
                a.append(i)
                break
    return a[n]
