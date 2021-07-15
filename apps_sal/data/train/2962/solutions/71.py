def divisible_by(numbers, divisor):
    arr = []
    for element in numbers:
        if element % divisor == 0:
            arr.append(element)
    return arr
