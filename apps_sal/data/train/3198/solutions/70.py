def check_exam(arr1, arr2):
    score = 0
    for c, s in zip(arr1, arr2):
        if s == "":
            score += 0
        elif s == c:
            score += 4
        else:
            score -= 1
    return score if score > 0 else 0
