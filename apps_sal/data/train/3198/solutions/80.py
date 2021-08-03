def check_exam(arr1, arr2):
    score = 0
    for key, ans in zip(arr1, arr2):
        if key == ans:
            score += 4
        elif ans != "" and ans != key:
            score -= 1
    return score if score > 0 else 0
