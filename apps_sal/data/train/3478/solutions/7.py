def battle(player1, player2):

    if len(player1) > len(player2):
        min_creatures = len(player2)
    else:
        min_creatures = len(player1)
        
    i = min_creatures - 1
    while i >= 0:
        if player1[i][0] >= player2[i][1] and player2[i][0] >= player1[i][1]:
            del player1[i]
            del player2[i]
        elif player1[i][0] >= player2[i][1]:
            del player2[i]
        elif player2[i][0] >= player1[i][1]:
            del player1[i]
        i -= 1
    
    return {'player1': player1, 'player2': player2}
