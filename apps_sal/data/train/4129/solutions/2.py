def queue(queuers, pos):
    return sum((min(q, queuers[pos]) for q in queuers)) - sum((1 for q in queuers[pos + 1:] if q >= queuers[pos]))
