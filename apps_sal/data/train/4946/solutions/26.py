def house_numbers_sum(x):
    a = 0
    for i in x:
        a += i
        if i == 0:
            break
    return a
