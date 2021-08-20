def queue(queuers, pos):
    min = 0
    while queuers[pos] > 0:
        for i in range(0, len(queuers)):
            if queuers[i] > 0:
                queuers[i] -= 1
                min += 1
            if queuers[pos] == 0:
                break
    return min
