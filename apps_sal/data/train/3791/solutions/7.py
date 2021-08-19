def moment_of_time_in_space(moment):
    a = sum((int(i) for i in moment if i in '123456789'))
    b = sum((1 for i in moment if i not in '123456789'))
    return [a < b, a == b, a > b]
