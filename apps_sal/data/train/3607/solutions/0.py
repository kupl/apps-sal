def eq_sum_powdig(hMax, exp):
    return [i for i in range(2, hMax + 1) if i == sum(int(c) ** exp for c in str(i))]

