def div_con(x):

    diff = 0
    for num in x:
        if isinstance(num, int):
            diff += num
        else:
            diff -= int(num)

    return diff
