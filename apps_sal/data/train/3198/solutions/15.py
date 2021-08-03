def check_exam(arr1, arr2):
    points = 0
    for i in range(len(arr1)):
        points += 4 if arr1[i] == arr2[i] else 0 if arr2[i] == '' else -1
    return points if points > 0 else 0
