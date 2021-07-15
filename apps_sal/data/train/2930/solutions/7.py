def summation(num):
    if num > 1:
       return num + summation(num - 1)
    return 1
