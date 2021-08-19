def invert(lst):
    tableau = len(lst) * [0]
    for loop in range(len(lst)):
        tableau[loop] = -lst[loop]
    return tableau
