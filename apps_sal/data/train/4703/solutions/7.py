def bar_triang(A, B, C):
    return [round(sum(axis) / 3.0, 4) for axis in zip(A, B, C)]
