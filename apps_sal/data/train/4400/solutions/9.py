def minimum_steps(numbers, value):
    numbers.sort()
    sum = 0
    operations = 0
    for x in numbers:
        sum += x
        if sum >= value:
            break
        operations += 1
    return operations
