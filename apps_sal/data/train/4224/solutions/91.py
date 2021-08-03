def dont_give_me_five(start, end):
    n = 0
    five = '5'
    for i in range(start, end + 1):
        i = str(i)
        if five in i:
            continue
        else:
            n += 1
    return n   # amount of numbers
