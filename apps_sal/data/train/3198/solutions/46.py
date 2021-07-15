def check_exam(arr1,arr2):
    score = 0
    for s in range (0, len(arr1)):
        for a in range (0, len(arr2)):
            if s == a :
                if arr1[s] == arr2[a]:
                    score += 4
                elif arr2[a] == "":
                    score += 0
                elif arr1[s] != arr2[a] :
                    score -= 1 
    if score < 0:
         return 0
    else:
         return score
  

