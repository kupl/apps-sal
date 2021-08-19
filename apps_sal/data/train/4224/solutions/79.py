def dont_give_me_five(start, end):
    count = 0
    while start <= end:
        if str(start).find('5') == -1:
            count += 1
        start += 1
    return count
