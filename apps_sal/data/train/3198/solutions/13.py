def check_exam(arr1, arr2):
    point = 0
    for e in list(zip(arr1, arr2)):
        point += 4 if e[0] == e[1] else(0 if e[1] == ''else -1)
    return 0 if point < 0 else point
