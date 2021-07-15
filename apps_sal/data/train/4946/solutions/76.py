def house_numbers_sum(inp):
    sum = 0
    for num in inp:
        if num != 0:
            sum += num
        else:
            return sum
            break
