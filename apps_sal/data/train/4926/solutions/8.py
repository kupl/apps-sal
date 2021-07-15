def only_one(*bool):
    sum = 0
    for value in bool:
        if value:
            sum += 1
    if sum == 1:
        return True
    else:
        return False
