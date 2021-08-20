def distribute(nodes, workload):
    ((q, r), it) = (divmod(workload, nodes), iter(range(workload)))
    return [[next(it) for _ in range(q + (n < r))] for n in range(nodes)]
