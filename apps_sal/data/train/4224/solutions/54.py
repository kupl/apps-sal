def dont_give_me_five(start, end):
    rc = 0
    for ing in range(start, end + 1):
        if '5' in list(str(ing)):
            pass
        else:
            rc += 1
    return rc
