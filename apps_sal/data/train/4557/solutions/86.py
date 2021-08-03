def row_weights(array):
    # create totals for each team
    total1 = 0
    total2 = 0
    # loop through array
    for x in range(len(array)):
        if x % 2 == 1:  # if odd number index, add to team2
            total2 += array[x]
        else:  # add to team1
            total1 += array[x]
    # combine results in a tuple
    return tuple((total1, total2))
