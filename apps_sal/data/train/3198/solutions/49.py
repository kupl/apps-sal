def check_exam(arr1,arr2):
    score = 0
    for i in range(4):
        if arr1[i] == arr2[i]:
            score = score + 4
        elif arr2[i] == "":
            score = score
        else:
            score = score - 1
    if score < 0:
        score = 0
    return score
  

