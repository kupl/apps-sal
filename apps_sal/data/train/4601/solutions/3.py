def mormons(starting_number, reach, target):
    return 0 if starting_number>=target else 1+mormons(starting_number*(1+reach), reach, target)
