def queue(queuers,pos):
    return sum(min(queuer, queuers[pos] - (place > pos)) for place, queuer in enumerate(queuers))
