def dont_give_me_five(start, end):
    count = 0
    for n in range(start, end + 1):
        if "5" not in str(n):
            count = count + 1
    return count
