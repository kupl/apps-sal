def dont_give_me_five(start, end):
    num = list(range(start, end + 1))
    count = 0
    for i in num:
        if "5" in str(i):
            pass
        else:
            count += 1
    return count
