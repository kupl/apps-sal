def check_exam(arr1, arr2):

    sum = 0
    for i, j in zip(arr1, arr2):
        if j == '':
            sum += 0
        elif i == j:
            sum += 4
        else:
            sum += -1

    if sum < 0:
        return 0
    else:
        return sum
