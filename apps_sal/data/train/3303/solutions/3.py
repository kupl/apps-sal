def div_con(x):
    sum = 0
    for i in x:
        if (type(i) == int):
            sum += i
        else:
            sum -= int(i)
    return sum
