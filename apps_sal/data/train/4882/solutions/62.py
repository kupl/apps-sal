def round_to_next5(n):
    counter = 0  

    if n > 0:
        while n > counter:
            counter += 5

            
        return counter      
    else:
        for i in range(n, -n+1):
            if i % 5 == 0:
                return i    

