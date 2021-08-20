def chromosome_check(sperm):
    sperm_list = list(sperm)
    if sperm_list[0] == sperm_list[1]:
        return "Congratulations! You're going to have a daughter."
    return "Congratulations! You're going to have a son."
