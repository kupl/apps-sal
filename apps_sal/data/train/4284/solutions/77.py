def array_leaders(numbers):
    res_list = []
    i = 0
    while i < len(numbers) - 1:
        if numbers[i] > sum(numbers[i + 1:]):
            res_list.append(numbers[i])
        i += 1
    if numbers[len(numbers) - 1] > 0:
        res_list.append(numbers[len(numbers) - 1])
    return res_list
