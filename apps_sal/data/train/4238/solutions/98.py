def squares_needed(grains):
    if grains == 0:
        return 0
    else:
        p = 1
        boxes = 1
        i = 1
        while i < grains:
            i += p * 2 
            p *= 2
            boxes += 1
        return boxes
            

