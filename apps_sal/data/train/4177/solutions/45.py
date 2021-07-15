def men_from_boys(arr):
    
    arr = list(dict.fromkeys(arr))
    
    men = []
    boys = []
    
    for i in arr:
        if i%2 == 0:
            men.append(i)
        else:
            boys.append(i)
    
    men.sort()
    boys.sort(reverse = True)
            
    return men + boys
