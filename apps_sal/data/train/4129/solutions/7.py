def queue(queuers, pos):
    count = 0
    while len(queuers) != 0:
        k = queuers.pop(0)
        count += 1
        if k - 1 != 0:
            queuers.append(k - 1)
            if pos == 0:
                pos = len(queuers) - 1
            else:
                pos -= 1
        elif k - 1 == 0 and pos == 0:
            break
        else:
            pos -= 1
    return count
