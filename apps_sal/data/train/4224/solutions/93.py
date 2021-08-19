def dont_give_me_five(start, end):
    itr = 0
    while start <= end:
        strNum = str(start)
        if "5" not in strNum:
            itr += 1
        start += 1
    return itr   # amount of numbers
