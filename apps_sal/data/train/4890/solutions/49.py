def find_difference(a, b):
    result=1
    result2=1
    for i in a: 
         result = result * i  
    for j in b: 
         result2 = result2 * j  
    
    return abs(result-result2)

