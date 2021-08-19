def check_exam(arr1, arr2):
    i = 0
    result = 0
    while i < len(arr1):
        if arr1[i] == arr2[i]:
            result = result + 4
        elif arr2[i] == '':
            result = result + 0
        else:
            result = result - 1
        i = i + 1
    if result < 0:
        return 0
    else:
        return result
