def dont_give_me_five(start, end):
    x = start
    total = 0
    while x < end + 1:
        if "5" not in str(x):
            total += 1
        x += 1
    return total
