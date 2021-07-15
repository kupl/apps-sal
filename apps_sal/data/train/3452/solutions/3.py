def snail(column, day, night):
    count = 0
    some = True
    while some:
        column = column - day
        if column <= 0:
            some = False
        column += night
        count += 1

    return count
