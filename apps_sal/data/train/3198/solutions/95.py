def check_exam(arr1, arr2):
    if len(arr1) != len(arr2):
        return 0
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == '':
            continue
        if arr1[i] == arr2[i]:
            score += 4
            continue
        if arr1[i] != arr2[i]:
            score -= 1
            continue
    return max(score, 0)
