def dont_give_me_five(start, end):
    position = start
    count = []

    while position <= end:
        if '5' in str(position):
            position += 1
        else:
            count.append(position)
            position += 1

    return len(count)
