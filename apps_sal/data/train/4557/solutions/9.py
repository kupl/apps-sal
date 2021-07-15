def row_weights(array):
    '''Calculate team 1 weights and team 2 weights
    separately, then return.'''
    
    # Team 1 weight
    team_1 = sum([array[x] for x in range(len(array)) if x % 2 == 0])
    
    # Team 2 weight
    team_2 = sum([array[x] for x in range(len(array)) if x % 2 != 0])
    
    # Return statement
    return(team_1, team_2)

