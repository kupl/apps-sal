def infected(s):
    total_population = s.split('X')
    total = 0
    infected = 0
    for population in total_population:
        if '1' in population:
            infected += len(population)
        total += len(population)
    try:
        return 100 * infected / total
    except ZeroDivisionError:
        return 0
