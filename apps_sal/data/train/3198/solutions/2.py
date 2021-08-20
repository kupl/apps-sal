def check_exam(arr1, arr2):
    score = 0
    for i in range(len(arr1)):
        if arr2[i] != '':
            if arr2[i] == arr1[i]:
                score = score + 4
            else:
                score = score - 1
    return score if score > 0 else 0
