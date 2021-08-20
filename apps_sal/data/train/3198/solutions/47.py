def check_exam(arr1='', arr2=''):
    x = 0
    for i in range(0, len(arr2), 1):
        if arr1[i] == arr2[i]:
            x = x + 4
        elif arr2[i] != arr1[i] and arr2[i] != '':
            x = x - 1
        else:
            x = x
    if x <= 0:
        return 0
    else:
        return x
