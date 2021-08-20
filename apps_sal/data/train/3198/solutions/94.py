def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr2)):
        if arr1[i] == arr2[i]:
            score = score + 4
        elif arr2[i] == '':
            score = score + 0
        elif arr1[i] != arr2[i]:
            score = score - 1
    if score < 0:
        return 0
    else:
        return score
