def row_sum_odd_numbers(n):
    num_pos = find_numb_count(n)
    sum = 0
    for i in range(n):
        sum += num_pos * 2 - 1
        num_pos -= 1
    return sum


def find_numb_count(n):
    if n == 1:
        return 1
    return find_numb_count(n - 1) + n
