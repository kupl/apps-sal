def starting_mark(height):

    height_1 = 1.52
    height_2 = 1.83
    start_1 = 9.45
    start_2 = 10.67
    
    v_constant = (start_2 - start_1) / (height_2 - height_1)
    
    start = start_1 + v_constant * (height - height_1)
    
    return round(start,2)
