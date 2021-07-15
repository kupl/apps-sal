def get_real_floor(n):
    if n <= 0:
        return n
    
    else:
        ans = n - 1
        
    if n > 13:
        ans = ans - 1
    
    return ans
