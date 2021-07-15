def sum_it_up(numbers_with_bases):
    return sum(int(number, base) for number, base in numbers_with_bases)
