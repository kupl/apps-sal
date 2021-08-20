def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] == '':
            continue
        elif arr2[i] != arr1[i]:
            score -= 1
        else:
            score += 4
    return max(score, 0)
