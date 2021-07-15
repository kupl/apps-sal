def check_exam(arr1,arr2):
    c = 0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            c += 4
        elif arr2[i] == '':
            c += 0
        else:
            c -= 1
    if c < 0:
        return 0
    else:
        return c
