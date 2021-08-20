def seven(m):
    (steps, lastdig, next) = (0, m % 10, m)
    while next > 99:
        next = next // 10 - lastdig * 2
        lastdig = next % 10
        steps += 1
    return (next, steps)
