def points(games): 
    total = 0
    a = len(games) 
    for i in range(0,a): 
            a = games[i].split(':') 
            if a[0] > a[1]: 
                total = total + 3 
            if a[0] == a[1]: 
                total = total + 1 
            if a[0] < a[1]: 
                total = total + 0 
    return total

