def zeros(n):
    import math
    ZEROS = 0
    
    if n == 0:
        return 0
    else:
        k_max = math.floor(math.log(n,5))        
        for k in range(1, k_max+1):
            ZEROS += n//(5**k)
        return ZEROS
