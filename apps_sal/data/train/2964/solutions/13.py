def sum_two_smallest_numbers(numbers):
    # your code here

    low1 = numbers[0]
    low2 = numbers[1]

    for i in numbers:
        if i < low1:
            low1 = i

    for i in numbers[1:]:
        if i < low2:
            if i != low1:
                low2 = i

    sum = low1 + low2

    return(sum)
