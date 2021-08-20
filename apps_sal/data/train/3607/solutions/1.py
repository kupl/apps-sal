def eq_sum_powdig(hMax, exp):
    ret = []
    for i in range(10, hMax + 1):
        if i == sum((int(j) ** exp for j in str(i))):
            ret.append(i)
    return ret
