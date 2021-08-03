def divisible_by(numbers, divisor):
    multiples = []
    for num in numbers:
        if num % divisor == 0:
            multiples.append(num)

    return multiples
