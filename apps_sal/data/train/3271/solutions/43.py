def arr(n=0):
    # [ the numbers 0 to N-1 ]
    lst = []
    for num in range(0, n):
        if num not in lst:
            lst.append(num)
        else:
            return ''

    return lst
