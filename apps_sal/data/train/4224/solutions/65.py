def dont_give_me_five(start, end):
    count = 0
    for i in range(start, end + 1):
        if str(i).find('5') == -1:
            count += 1
    return count
