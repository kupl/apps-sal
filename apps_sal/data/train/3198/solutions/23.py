def check_exam(arr1,arr2):
    score = 0
    for elt1, elt2 in zip(arr1, arr2) :
        if not elt2 :
            pass
        elif elt1 == elt2 :
            score += 4
        else :
            score -=1
    return max(score, 0)
        
  

