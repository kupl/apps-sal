def chromosome_check(sperm):
    b = "Congratulations! You're going to have a son."
    g = "Congratulations! You're going to have a daughter."
    if sperm == 'XY':
        return b
    else:
        return g
