def house_numbers_sum(inp):
    sum = 0
    for number in inp:
        sum += number
        if number == 0:
            break
    return sum
