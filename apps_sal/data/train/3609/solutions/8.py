def is_onion_array(a):
    print(a)
    for num in range(len(a)):
        if a[num] !=a[-(num+1)]:
            if not a[num] + a[-(num + 1)] <=10:
                return False
        
            
        
    
    return True
