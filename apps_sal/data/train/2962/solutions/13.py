def divisible_by(numbers, divisor):
    scores = []
    for number in numbers:
        if number % divisor == 0:
            scores.append(number)
    return scores
