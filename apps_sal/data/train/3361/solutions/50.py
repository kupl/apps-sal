def sum_of_minimums(numbers):
    rs = 0
    for i in numbers:
        rs += min(i)
    return rs
