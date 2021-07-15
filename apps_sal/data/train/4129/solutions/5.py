def queue(queuers, pos, time = 0):
    while True:
        for i in range(len(queuers)):
            if queuers[pos] == 0:
                return time
            elif queuers[i]:
                queuers[i] -= 1
                time += 1
