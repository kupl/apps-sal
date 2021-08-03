def tidyNumber(n):
    lst = [x for x in list(str(n))]
    lst1 = sorted(lst, key=int)
    return int(''.join(lst1)) == n
