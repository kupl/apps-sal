def dont_give_me_five(s, e):
    count = 0
    for x in range(s, e + 1):
        if str(5) not in str(x):
            count += 1
    return count
