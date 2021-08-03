def n_linear(m, n):
    if n == 0:
        return 1
    init, dicto = [1], {}.fromkeys(m, 0)
    for i in range(n):
        dd = min(k * init[dicto[k]] + 1 for k in dicto)
        init.append(dd)
        for k in dicto:
            dicto[k] += init[dicto[k]] * k + 1 == dd
    return dd
