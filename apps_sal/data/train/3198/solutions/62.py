def check_exam(arr1,arr2):
    mark = 0
    for a1, a2 in zip(arr1, arr2):
        if a1 == a2:
            mark += 4
        elif a1 != a2 and a2 != '':
            mark -=1
    return 0 if mark < 0 else mark

