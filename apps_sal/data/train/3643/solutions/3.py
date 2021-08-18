def distribute(nodes, workload):
    div, mod = divmod(workload, nodes)
    def breakpoint(i): return i * div + (i if i < mod else mod)
    return [list(range(breakpoint(i), breakpoint(i + 1))) for i in range(nodes)]
