AVAILABLE_METHODS = {
    'even': lambda x: x / 2,
    'odd': lambda x: 3 * x + 1
}


def generator(x):
    temp = x
    temp_num = 0
    while temp > 1:
        if temp % 2 == 0:
            temp = AVAILABLE_METHODS['even'](temp)
        else:
            temp = AVAILABLE_METHODS['odd'](temp)
        temp_num += 1
        yield temp_num


def longest_collatz(input_array):
    answer_list = [sum([item for item in generator(dig)]) for dig in input_array]
    print(max(answer_list), answer_list)
    return input_array[(answer_list.index(max(answer_list)))]
