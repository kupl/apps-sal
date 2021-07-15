def sum_it_up(numbers_with_bases):
    return sum(list(map(lambda x: int(x[0], x[1]), numbers_with_bases)))
