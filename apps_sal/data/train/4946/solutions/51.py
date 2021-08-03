def house_numbers_sum(lst):
    result = 0
    for num in lst:
        if num == 0:
            return result
        result += num
