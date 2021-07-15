def row_weights(array):
    #numbers are switched because I am "smart" and lazy. idk anymore man, it works.
    team2 = 0
    team1 = 0    
    for i in range(len(array)):
        if i == 0:
            team1 = team1 + array[i]
            team2 = team2
        elif i % 2 != 0 and i > 0:
            team2 = team2 + array[i]
        elif i % 2 == 0 and i > 0:
            team1 = team1 + array[i]
            
    return (team1, team2)

