def queue(q, pos):
    return (
        sum(min(x, q[pos]) for x in q[:pos + 1]) +
        sum(min(x, q[pos] - 1) for x in q[pos + 1:])
    )
