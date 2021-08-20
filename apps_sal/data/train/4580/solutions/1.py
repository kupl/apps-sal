def tiaosheng(failed_counter):
    count = 0
    jumps = 0
    while count < 60:
        count += 1
        jumps += 1
        if jumps in failed_counter:
            count += 3
    return jumps
