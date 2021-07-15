def row_weights(array):
    y = 2
    team1,team2 = 0,0
    
    for i in array:
        if y%2==0:
            team1 += i   
            y+=1
        else:
            team2 += i   
            y+=1    
    return (team1,team2)        
