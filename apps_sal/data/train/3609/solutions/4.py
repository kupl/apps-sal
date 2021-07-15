def is_onion_array(a):
    for j in range(len(a)//2):
        if a[j] + a[-j-1] > 10:
            return False
    return True
    
    

