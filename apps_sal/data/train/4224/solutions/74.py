def dont_give_me_five(start,end):
    count = 0
    for i in list(range(start, end + 1)):
        if '5' not in str(i):
            count += 1
    return count
