def queue(queuers, pos):
    friendWait = queuers[pos]
    frontOfLine = queuers[:pos + 1]
    backOfLine = queuers[pos + 1:]
    frontOfLine = [min(x, friendWait) for x in frontOfLine]
    backOfLine = [min(x, friendWait - 1) for x in backOfLine]
    return sum(frontOfLine) + sum(backOfLine)
