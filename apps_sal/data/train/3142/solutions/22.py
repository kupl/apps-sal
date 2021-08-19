def seven_ate9(input):
    while '797' in input:
        position = input.find('797')
        input = input[0:position] + '77' + input[position + 3:]
    return input
