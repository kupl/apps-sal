def check_exam(arr1,arr2):
    score = 0
    for i in range(0,len(arr1)):
        if not arr2[i]: continue
        if arr1[i] == arr2[i]: score += 4
        elif arr1[i] != arr2[i]: score -= 1
    if score < 0: score = 0
    return score
