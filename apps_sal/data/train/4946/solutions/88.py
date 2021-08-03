def house_numbers_sum(inp):
    result = 0
    for number in inp:
        result += number
        if number == 0:
            break

    return result
