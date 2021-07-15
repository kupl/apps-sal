def row_sum_odd_numbers(n):
    row_generator = generate_row(n)
    sum = 0
    for val in row_generator:
        sum += val
    return sum


def generate_row(i: int):
    start = i * (i - 1) + 1
    row_length = i
    for num in range(row_length):
        yield start
        start += 2
