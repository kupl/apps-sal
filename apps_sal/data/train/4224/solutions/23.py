def dont_give_me_five(start, end):
    z = 0
    for i in range(start, end + 1):
        if str(i).find('5') == -1:
            z += 1
    return z
