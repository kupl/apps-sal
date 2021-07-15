def tiaosheng(failed_counter):
    time = 0
    for i in range(1, 61):
        if time >= 60:
            return i-1
        time += 1
        if i in failed_counter:
            time += 3
    return i
