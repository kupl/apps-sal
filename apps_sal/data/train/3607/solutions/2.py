def eq_sum_powdig(hmax, exp):
    return [i for i in range(2, hmax + 1) if sum(int(d) ** exp for d in str(i)) == i]
