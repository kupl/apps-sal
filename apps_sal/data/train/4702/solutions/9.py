def digits_product(product):
    if product < 10:
        return 10 + product
    
    facs = []
    
    for p in (2,3,5,7):
        while product % p == 0:
            facs.append(p)
            product //= p
    
    if product != 1:
        return -1
    
    while facs.count(3) >= 2:
        facs.remove(3)
        facs.remove(3)
        facs.append(9)
    
    while facs.count(2) >= 3:
        facs.remove(2)
        facs.remove(2)
        facs.remove(2)
        facs.append(8)
    
    while 2 in facs and 3 in facs:
        facs.remove(2)
        facs.remove(3)
        facs.append(6)
    
    while facs.count(2) >= 2:
        facs.remove(2)
        facs.remove(2)
        facs.append(4)
    
    return int("".join(sorted(str(x) for x in facs)))
        

