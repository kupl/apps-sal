def shared_bits(a, b):
    result = b & a
    commun = 0
    
    for i in range(0, 17):
        if (result & pow(2,i)) != 0:
            commun += 1
    if commun >= 2:
        return True
    else:
        return False
    return
