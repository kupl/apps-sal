def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            if arr2[i] != "":
                score -= 1
        else:
            score += 4
    return score if score > 0 else 0
