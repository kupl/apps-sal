def house_numbers_sum(inp):
    sum_ = 0
    for num in inp:
        if num != 0:
            sum_ += num
        else:
            break
    return sum_
