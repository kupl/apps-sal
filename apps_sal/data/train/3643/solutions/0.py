def distribute(nodes, workload):
    w = list(range(workload))[::-1]
    return [[w.pop() for _ in range(workload // nodes + (workload % nodes > n))] for n in range(nodes)]
