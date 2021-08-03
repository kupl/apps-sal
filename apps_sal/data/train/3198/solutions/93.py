def check_exam(arr1, arr2):
    if len(arr1) == len(arr2) and arr1 != [] and arr2 != []:
        score = 0
        for a in range(len(arr1)):
            if arr2[a] == '':
                continue
            elif arr1[a] == arr2[a]:
                score += 4
            else:
                score -= 1
        if score < 0:
            score = 0

    return score
