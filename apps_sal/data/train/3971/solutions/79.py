def tidyNumber(n):
    digits=[int(d) for d in str(n)]
    
    for i in range(len(digits)-1):
        if digits[i]>digits[i+1]:
            return False
    
    return True
