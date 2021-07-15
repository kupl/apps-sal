def check(seq, elem):
    counter = 0 
    for i in seq: 
        if elem == i: 
            counter += 1
    if counter > 0: 
        return True 
    else: 
        return False

