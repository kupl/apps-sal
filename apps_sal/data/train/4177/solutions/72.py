def men_from_boys(arr):
    men = []
    boy = []
    
    for el in arr:
        if el % 2==0 and el not in men:
            men.append(el)
        elif el % 2 != 0 and el not in boy:
            boy.append(el)
            
    return sorted(men) + sorted(boy,reverse=True) 
