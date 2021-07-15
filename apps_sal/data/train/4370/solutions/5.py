def indices(n, d):
    if n == 1: return [[d]]
    if d == 0: return [[0 for i in range(n)]]
    sols = []
    for i in range(d+1):
        sols += [subsol + [i] for subsol in indices(n-1,d-i)]
    
    return sols
    raise NotImplementedError('todo')
