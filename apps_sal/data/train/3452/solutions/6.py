def snail(column, day, night):
    total = 0
    when = True
    n = 0
    while column > total:
        if when:
            total += day
            when = False
            n += 1
        else:
            total -= night
            when = True
    return n
