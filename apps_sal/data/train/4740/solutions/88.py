def row_sum_odd_numbers(n):
    counter = 0
    start_number = 1
    end_number = 1
    sum_ = 1
    for i in range(n - 1):
        start_number += counter + 2
        end_number += counter + 4
        sum_ = sum([x for x in range(start_number, end_number + 2) if x % 2 != 0])
        counter += 2
    return sum_
