# Why do we fall ? So we can learn to pick ourselves up.


t = int(input())
for _ in range(0, t):
    n = int(input())
    abc = [int(i) for i in input().split()]

    i = 0

    lst = [n]

    for _ in range(0, 100):
        k = str(lst[-1] / abc[i % 3]).split('.')
        if int(k[1][0]) > 0:
            lst.append(int(k[1][0]))
        else:
            lst.append(int(k[0][0]))
        i += 1
    pattern = []
    ind = 0
    while len(pattern) == 0:
        for i in range(ind, len(lst) - 1):
            check = lst[ind: i + 1] * 50
            check = check[:len(lst) - ind]
            if lst[ind:] == check:
                pattern = check
                break
        if len(pattern):
            break
        ind += 1
    final_pattern = []
    for i in range(0, len(pattern)):
        couldbe = pattern[:i + 1]
        check = pattern[:i + 1] * 100
        check = check[:len(pattern)]
        if check == pattern:
            final_pattern = couldbe
            break
    lp = len(final_pattern)
    q = int(input())
    for _ in range(0, q):
        qq = int(input())
        if qq < ind:
            print(lst[qq])
        else:
            qq -= ind
            kk = qq % lp
            print(final_pattern[kk])


"""
1
56
3 5 7
4
0
1
2
3

"""
