def sum_two_smallest_numbers(A):
    return sum(sorted([x for x in A if x > 0])[:2])
