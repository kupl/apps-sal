def check_exam(arr1,arr2):
    score = 0
    for i,j in zip(arr1,arr2):
        if j == "":
            continue
        elif i == j:
            score += 4
        elif i != j:
            score -= 1
        else:
            pass
    if score <= 0:
        return 0
    else:
        return score
    pass
  

