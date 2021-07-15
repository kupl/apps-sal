def check_exam(arr1,arr2):
    score = 0
    for x in range(len(arr1)):
        if arr1[x] == arr2[x]:
            score += 4
        elif arr2[x] != "" and arr2[x] != arr1[x]:
            score -= 1
    if score < 0:
        score = 0
    return score
