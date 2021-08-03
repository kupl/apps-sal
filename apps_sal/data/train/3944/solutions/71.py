def sum_triangular_numbers(n):
    sum_list = [0]
    for i in range(1, n + 1):
        sum_list.append(sum_list[-1] + i)
    return sum(sum_list)
