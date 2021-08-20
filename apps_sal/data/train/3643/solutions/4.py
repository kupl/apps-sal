from itertools import accumulate, tee


def distribute(nodes, workload):
    (q, r) = divmod(workload, nodes)
    ns = [q + (i < r) for i in range(nodes)]
    xs = list(accumulate([0] + ns))
    return [list(range(i, j)) for (i, j) in zip(xs, xs[1:])]
