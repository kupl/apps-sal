def sum_even_numbers(seq):
    to_sum = [num for num in seq if num % 2 == 0]
    return sum(to_sum)
