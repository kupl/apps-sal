import numpy


def check_exam(arr1, arr2):
    result = 0
    for i in range(len(arr2)):
        if arr1[i] == arr2[i]:
            result += 4
        else:
            result -= 1
    result += arr2.count('')
    return 0 if result < 0 else result
