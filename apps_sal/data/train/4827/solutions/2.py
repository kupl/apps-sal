def stats_disc_distr(arr):
    a = round(sum(float(i[1]) for i in arr),2) != 1
    b = not all(int(i[0])==i[0] for i in arr)
    if a and b : return "It's not a valid distribution and furthermore, one or more variable value are not integers"
    if a :       return "It's not a valid distribution"
    if b :       return "All the variable values should be integers"
    _mean = sum(i[0]*i[1] for i in arr)
    _var = sum(((i[0]-_mean)**2)*i[1] for i in arr)
    _sdt = _var ** .5
    return [_mean, _var, _sdt]
