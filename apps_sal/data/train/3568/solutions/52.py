def bumps(road):
    ncount = 0
    a = [char for char in road]
    for i in range(len(a)):
        if a[i] == "n":
            ncount += 1
            
    if ncount > 15:
        return "Car Dead"
    else:    
        return "Woohoo!"
