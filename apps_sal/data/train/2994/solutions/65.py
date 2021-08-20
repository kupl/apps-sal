def find_digit(num, nth):
    num1 = abs(num)
    res = [int(x) for x in str(num1)]
    nnum = len(res)
    if nth <= 0:
        return -1
    if nth > nnum:
        return 0
    else:
        return res[-nth]
