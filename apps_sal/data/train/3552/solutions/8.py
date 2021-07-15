def update_score(current_score, called_trump, alone, tricks):
    tricks_won = sum([int(val / called_trump)  for val  in tricks if val == called_trump])
    if alone and tricks_won == 5: points_won = 4
    elif tricks_won == 5:  points_won = 2
    elif tricks_won == 5:  points_won = 2
    elif tricks_won >=3 :  points_won = 1
    else:
        points_won = 2
        if called_trump == 1:called_trump = 2
        else: called_trump = 1
    current_score[called_trump-1] = current_score[called_trump-1] + points_won
    return current_score
