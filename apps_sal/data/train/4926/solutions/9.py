def only_one(*bools):
    return sum(x for x in bools) == 1
