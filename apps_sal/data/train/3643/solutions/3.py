def distribute(nodes, workload):
    div, mod = divmod(workload, nodes)
    def breakpoint(i): return i * div + (i if i < mod else mod)
    return [list(range(breakpoint(i), breakpoint(i + 1))) for i in range(nodes)]


# one-liner
# def distribute(n, w):
#    return [list(range(i*(w//n)+w%n-max(0, w%n-i), (i+1)*(w//n)+w%n-max(0, w%n-i-1))) for i in range(n)]
