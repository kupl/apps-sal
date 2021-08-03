def check_exam(arr1, arr2):
    points = 0
    for n in range(len(arr1)):
        if arr2[n] != '':
            if arr1[n] == arr2[n]:
                points = points + 4
            else:
                points = points - 1
    if points < 0:
        points = 0
    return points
