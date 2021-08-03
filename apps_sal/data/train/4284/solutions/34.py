def array_leaders(numbers):
    accum = 0
    leaders = []

    for n in reversed(numbers):
        if n > accum:
            leaders.append(n)
        accum += n
    leaders.reverse()

    return leaders
