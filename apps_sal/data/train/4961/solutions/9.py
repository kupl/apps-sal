def box(A):
    return (lambda X, Y: {'nw': [max(X), min(Y)], 'se': [min(X), max(Y)]})(*zip(*A))
