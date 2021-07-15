def check_exam(arr1,arr2):
    sum = 0
    for a,b in zip(arr1, arr2):
        if a==b:
            sum+=4
        elif b == '':
            sum+=0
        else:
            sum-=1
    if sum<0:
        return 0
    else:
        return sum
    
                
                
  

