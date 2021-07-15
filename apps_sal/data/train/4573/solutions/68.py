def over_the_road(address, n):
    if address % 2 == 0: 
        high_even = n * 2           
        count = (high_even - address)/2  
        return (count * 2) + 1    
    else:
        high_odd = (n * 2) - 1       
        count = (high_odd - address)/2 
        return (count * 2) + 2
