def row_sum_odd_numbers(n):
    # your code here
    first_num = 1 + n * (n - 1)
    last_num = first_num + 2 * (n - 1)
    new_list = [x for x in range(first_num, last_num + 1) if (x + 1) % 2 == 0]
    return sum(new_list)
