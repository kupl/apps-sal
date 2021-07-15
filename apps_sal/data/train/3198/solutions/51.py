def check_exam(arr1,arr2):
    n = len(arr1)
    score = 0
    while n > 0:
        n -= 1
        if arr2[n] == "":
            score = score
        elif arr2[n] == arr1[n]:
            score += 4
        else: score -= 1
    return max(score,0)
