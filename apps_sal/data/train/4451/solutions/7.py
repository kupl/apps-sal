def golf_score_calculator(par_string, score_string):
    # Convert each string into a list of integers
    par_list = list(map(int, par_string))
    score_list = list(map(int, score_string))

    # Use a for loop thru both lists to calculate difference for each hole
    differences = [i - j for i, j in zip(score_list, par_list)]

    # Summate all values in differences list for score
    return sum(differences)
    pass
