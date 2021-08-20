def row_sum_odd_numbers(n):
    total_nums = sum(range(0, n + 1))
    num_array = []
    count = 1
    while True:
        if count % 2 != 0:
            num_array.append(count)
        if len(num_array) == total_nums:
            break
        count += 1
    return sum(num_array[-n:])
