def divisible_by(numbers, divisor):
    output = []
    for element in numbers:
        if element % divisor == 0:
            output.append(element)
    return output
