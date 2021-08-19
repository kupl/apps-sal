def row_sum_odd_numbers(num_line):
    sum_permid = 0
    first_line = num_line * (num_line - 1) + 1
    stop_line = first_line + (num_line) * 2
    for j in range(first_line, stop_line, 2):
        sum_permid += j
    return sum_permid
# your code here
