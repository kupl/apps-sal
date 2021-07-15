def sum_it_up(numbers_with_bases):
    output = []
    for number in numbers_with_bases:
        output.append(int(number[0],number[1]))
    return sum(output)
