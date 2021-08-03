def summation(num, sums=0):
    if num == 0:
        return sums
    else:
        return summation(num - 1, sums + num)
