def custom_fib(ini, index, k):
    for n in range(k - len(ini) + 1):
        ini = ini[1:] + [sum(ini[i] for i in index)]
    return ini[[-1, k][k < len(ini)]]
