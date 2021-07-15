
def best_match(goals1 : list, goals2 : list):

    # Set the current "best" values as the first match
    lowest_difference = goals1[0] - goals2[0]
    amount_of_goals = goals2[0]
    best_match_index = 0

    # Loop through the length of the lists, to see if theres a better match
    for i in range(1, len(goals1)):

        # The current difference in goals.
        current_difference = goals1[i] - goals2[i]

        if (current_difference) < lowest_difference: # If the game was closer, this is the best match
            lowest_difference = current_difference
            amount_of_goals = goals2[i]
            best_match_index = i

        elif (current_difference == lowest_difference) and (amount_of_goals < goals2[i]): # If the difference is the same, but Zamalek scored more goals, it should change the best match.
            amount_of_goals = goals2[i]
            best_match_index = i
    
    return best_match_index
