def summation(num):
    if num == 1:
        return 1
    return summation(num-1) + num
