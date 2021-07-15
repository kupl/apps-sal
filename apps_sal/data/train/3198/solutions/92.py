def check_exam(arr1,arr2):
    score = 0
    for i in range(len(arr1)):
        validAnswer = arr1[i]
        studentAnswer = arr2[i]
        if studentAnswer == '':
            continue
            
        if studentAnswer == validAnswer:
            score += 4
        else:
            score -= 1
    if score < 0:
        return 0
    else:
        return score
    pass
    
  

