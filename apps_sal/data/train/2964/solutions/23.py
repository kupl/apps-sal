def sum_two_smallest_numbers(numbers):
    (n1, n2) = (numbers[0], numbers[1])
    for i in numbers[2:]:
        if n2 < n1:
            (n2, n1) = (n1, n2)
        if i < n2:
            n2 = i
    return n1 + n2
