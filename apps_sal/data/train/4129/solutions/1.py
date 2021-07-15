def queue(queuers,pos):
    friendWait = queuers[pos]
    # Divide the line into the front of the line (up to the friend)
    # and back of the line (behind the friend):
    frontOfLine = queuers[:pos+1]
    backOfLine = queuers[pos+1:]
    # Convert the frontOfLine to the min of friendWait:
    frontOfLine = [min(x, friendWait) for x in frontOfLine]
    # Convert the backOfLine to the min of friendWait-1:
    backOfLine = [min(x, friendWait-1) for x in backOfLine]
    # Return the result, which is the sum of both line parts:
    return sum(frontOfLine) + sum(backOfLine)

