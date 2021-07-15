def points(games):
    
    points = 0
    
    for i in range (len(games)) :
        match = games[i]
        x = match[0]
        y = match[2]
        
        if x > y : points += 3
        elif x == y : points += 1
    
    return points

points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])
