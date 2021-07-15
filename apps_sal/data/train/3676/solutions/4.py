def sum_it_up(numbers_with_bases):
    return sum(int(num, base) for num, base in numbers_with_bases)
