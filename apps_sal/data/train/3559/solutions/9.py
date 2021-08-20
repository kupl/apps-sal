def chromosome_check(sperm):
    if all((i == sperm[0] for i in sperm)):
        return "Congratulations! You're going to have a daughter."
    return "Congratulations! You're going to have a son."
