def odd_or_even(arr):
    list = [i for i in arr]
    su = sum(list)
    if su == 0:
        return 'even'
    elif su % 2 == 0:
        return 'even'
    else:
        return 'odd'
