def chromosome_check(sperm):
    gender = 'son' if 'Y' in sperm else 'daughter'
    return "Congratulations! You're going to have a {}.".format(gender)
