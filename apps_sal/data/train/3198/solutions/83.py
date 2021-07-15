def check_exam(arr1,arr2):
    grade = 0
    
    counter = len(arr1)
    
    scores = 0
    
    while scores < counter:
        if arr1[scores] == arr2[scores]:
            grade = grade + 4
        elif arr1[scores] == "" or arr2[scores] == "":
            grade = grade + 0
        else:
            grade = grade - 1
        
        scores+=1
    
    if grade < 0:
        return 0
    else:
        return grade
            
    
  

