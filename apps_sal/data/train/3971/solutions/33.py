def tidyNumber(n):
    for i,c in enumerate(str(n)):
        if i!=0:
            if c < str(n)[i-1]:
                return False
            
    return True

