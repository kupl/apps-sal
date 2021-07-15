def row_weights(array):
    team_1_weight = sum(array[0::2])
    team_2_weight = sum(array[1::2])
    total_weights_tuple = (team_1_weight, team_2_weight)
    return total_weights_tuple
