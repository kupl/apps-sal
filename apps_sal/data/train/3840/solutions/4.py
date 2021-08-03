from math import sqrt as s


def largest_power(n):
    if n == 1:
        return (0, -1)
    elif n <= 4:
        return (1, -1)
    else:
        alist = []
        for i in range(2, round(s(n) + 2)):
            j = int(1)
            while i**j < n:
                a = i**j
                j += 1
            alist.append(a)
            aset = (max(alist), alist.count(max(alist)))
    return aset
