def divisible_by(numbers, divisor):
    return list(numbers[i] for i in range(len(numbers)) if numbers[i] % divisor == 0)
