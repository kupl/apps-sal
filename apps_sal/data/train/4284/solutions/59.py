def array_leaders(numbers):
    final_list = []
    for item in range(len(numbers)):
        if numbers[item] > sum(numbers[item+1:]):
            final_list.append(numbers[item])
    return final_list
