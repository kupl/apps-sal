def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)
