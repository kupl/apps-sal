def check_exam(arr1, arr2):
    k = 0
    for x in range(len(arr1)):
        if arr2[x] != '':
            if arr1[x] == arr2[x]:
                k += 4
            else:
                k -= 1
    if k < 1:
        return 0
    return k
