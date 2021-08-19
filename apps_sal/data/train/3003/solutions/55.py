def args_count(*therest, **alsorest):
    """
    x - numeric arguments
    returns - count of agruments passed
    """
    count = 0
    for n in therest:
        count += 1
    for m in alsorest:
        count += 1
    return count
