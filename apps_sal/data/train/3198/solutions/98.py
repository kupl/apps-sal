def check_exam(arr1,arr2):
    score0 = 0
    score1 = 0
    score2 = 0
    score3 = 0
    if arr1[0] == arr2[0]:
        score0 = 4
    elif arr2[0]=="":
        score0 = 0
    elif arr1[0] != arr2[0]: 
        score0 = -1
    
    if arr1[1] == arr2[1]:
        score1 = 4
    elif arr2[1]=="":
        score1 = 0
    elif arr1[1] != arr2[1]: 
        score1 = -1
    
    if arr1[2] == arr2[2]:
        score2 = 4
    elif arr2[2]=="":
        score2 = 0
    elif arr1[2] != arr2[2]: 
        score2 = -1
        
    if arr1[3] == arr2[3]:
        score3 = 4
    elif arr2[3]=="":
        score3 = 0
    elif arr1[3] != arr2[3]: 
        score3 = -1
        
    totalscore = score0+score1+score2+score3
    
    if totalscore < 0:
        return 0
    else:
        return totalscore
  

