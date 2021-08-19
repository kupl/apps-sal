from operator import itemgetter


def fib_digits(n):
    a, b = 1, 1
    num = n
    num_int = int(num - 2)
    for i in range(num_int):
        a, b = b, a + b
    print(b)
    num = b
    print(num)
    lst = list(map(int, str(num)))
    lst2 = []
    p = False
    i = 1
    lst2.append([1, lst[0]])
    while i < len(lst):
        d = 0
        while d < len(lst2):
            if lst[i] == lst2[d][1]:
                #lst2[d][0] += 1
                p = True
                break
            d += 1
        if p == True:
            lst2[d][0] += 1
        else:
            lst2.append([1, lst[i]])
        i += 1
        p = False
    print(lst2)
    i = 0
    while i < len(lst2):
        lst2[i] = tuple(lst2[i])
        i += 1
    return(sorted((lst2), reverse=True))
