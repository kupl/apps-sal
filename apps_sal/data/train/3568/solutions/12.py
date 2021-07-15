def bumps(road):
    a = 0
    
    for i in road:
        if i == 'n':
            a += 1
            
    if a > 15:
        return 'Car Dead'
    else:
        return 'Woohoo!'
        

