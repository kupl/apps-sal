def sum_triangular_numbers(n):
    list = []
    count = 0
    for num in range(1, n + 1):
        count += num
        list.append(count)
    return sum(list)
