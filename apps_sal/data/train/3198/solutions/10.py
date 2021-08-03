def check_exam(arr1, arr2):
    score = 0
    for n, a in enumerate(arr2):
        if a != '':
            if a == arr1[n]:
                score += 4
            else:
                score -= 1
    return max(score, 0)
