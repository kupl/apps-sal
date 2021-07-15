def divisible_by(numbers, divisor):
    divisors = []
    for i in range(len(numbers)):
        if numbers[i] % divisor == 0:
            divisors.append(numbers[i])
    return divisors
