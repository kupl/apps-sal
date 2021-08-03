def check_exam(arr1, arr2):
    iterator = 0
    score = 0
    while iterator < 4:
        if arr1[iterator] == arr2[iterator]:
            score = score + 4
            iterator = iterator + 1
        elif arr1[iterator] != arr2[iterator] and arr2[iterator] != "":
            score = score - 1
            iterator = iterator + 1
        else:
            iterator = iterator + 1
    if score < 0:
        score = 0
    return score
