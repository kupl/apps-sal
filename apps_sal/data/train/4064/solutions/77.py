def count_by(x, n):
    
# =============================================================================
#     This function given two arguments returns an array of the first (n) multiples of (x). 
# 
#     Both the given number and the number of times to count will be positive 
#     numbers greater than 0.
#     
#     The function returns the result as a list.
#     Examples:
#         count_by(1,10) ==> [1,2,3,4,5,6,7,8,9,10]
#         count_by(2,5) ==>  [2,4,6,8,10]
# =============================================================================
        
    result = []
    
    for n in range(1,(n+1)):
        result.append(n * x)
    
    return result

