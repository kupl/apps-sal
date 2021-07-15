def check_exam(arr1,arr2):
    score=0
    for i,j in zip(arr1,arr2):
        if i==j:
            score+=4
        
        if j=="" and i!="":
            score+=0
        if i!="" and j!="" and i!=j:
            score-=1
    if score<0:
        return 0
    else:
        return score
  

