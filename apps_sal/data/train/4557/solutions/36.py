def row_weights(array):

    first_team = 0
    second_team = 0

    for x in range(len(array)):

        if x % 2 == 0:
            first_team += array[x]
        else:
            second_team += array[x]

    return (first_team, second_team)
