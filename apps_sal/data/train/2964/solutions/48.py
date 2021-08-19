def find_maximum(numbers):
    max_ = numbers[0]
    index = 0
    for (count, num) in enumerate(numbers):
        if num > max_:
            max_ = num
            index = count
    return index


def sum_two_smallest_numbers(numbers):
    top2 = [numbers[0], numbers[1]]
    max_index = find_maximum(top2)
    for num in numbers[2:]:
        if num < top2[max_index]:
            top2[max_index] = num
            max_index = find_maximum(top2)
    return top2[0] + top2[1]
