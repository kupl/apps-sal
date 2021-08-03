import numpy


def distribute(nodes, workload):
    return [list(i) for i in numpy.array_split(numpy.array(range(0, workload)), nodes)]
