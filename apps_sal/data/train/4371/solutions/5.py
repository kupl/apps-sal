def digits(num):
    num = str(num)
    return [int(x)+int(y) for n, x in enumerate(num,1) for y in num[n:]]

