def check_exam(arr1, arr2):

    q = 0
    for i, j in zip(arr1, arr2):
        if i == j:
            q += 4
        elif i != j and j != '':
            q -= 1
    if q > 0:
        return q
    else:
        return 0
