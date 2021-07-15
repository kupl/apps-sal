def two_highest(arg1):
    return [max(arg1), max(x for x in arg1 if x != max(arg1))] if len(arg1) > 1 else [] if arg1 == [] else arg1
