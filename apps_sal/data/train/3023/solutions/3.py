def best_match(goals1: list, goals2: list):
    lowest_difference = goals1[0] - goals2[0]
    amount_of_goals = goals2[0]
    best_match_index = 0
    for i in range(1, len(goals1)):
        current_difference = goals1[i] - goals2[i]
        if current_difference < lowest_difference:
            lowest_difference = current_difference
            amount_of_goals = goals2[i]
            best_match_index = i
        elif current_difference == lowest_difference and amount_of_goals < goals2[i]:
            amount_of_goals = goals2[i]
            best_match_index = i
    return best_match_index
