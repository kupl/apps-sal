def sum_two_smallest_numbers(numbers):
    x, y = numbers[:2]
    if x > y:
        x, y = y, x

    for z in numbers[2:]:
        if z < x:
            y = x
            x = z
        elif z < y:
            y = z

    return x + y
