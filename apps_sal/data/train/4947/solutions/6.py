def sel_number(n, d):
    # Longer, broken-up version
    def iterator_count(it): return sum(1 for _ in it)
    def check_constraints_1_and_3(a): return len(set(a)) == len(a) > 1
    def check_constraints_2_and_4(a): return all(int(y) - int(x) <= d and y > x for x, y in zip(a[:-1], a[1:]))
    numbers_iterator = map(str, xrange(n + 1))

    numbers_iterator = filter(check_constraints_1_and_3, numbers_iterator)
    numbers_iterator = filter(check_constraints_2_and_4, numbers_iterator)
    return iterator_count(numbers_iterator)
