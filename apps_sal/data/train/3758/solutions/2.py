def word_mesh(A, z=''):
    for (x, y) in zip(A, A[1:]):
        while not y.startswith(x):
            x = x[1:]
        if x == '':
            return 'failed to mesh'
        z += x
    return z
