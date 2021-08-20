def summation(num):
    if num == 1:
        return 1
    else:
        return num + summation(num - 1)


print(summation(6))
