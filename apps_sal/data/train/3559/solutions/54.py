def chromosome_check(sperm):
    if sperm[0] == 'X' and sperm[1] == 'X':
        return "Congratulations! You're going to have a daughter."
    elif sperm[0] == 'X' and sperm[1] == 'Y':
        return "Congratulations! You're going to have a son."
