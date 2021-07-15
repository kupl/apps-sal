def dont_give_me_five(start,end):
    counts = 0
    for num in range(start, end + 1):
        if '5' not in str(num):
            counts = counts + 1
        else:
            continue
    return counts
