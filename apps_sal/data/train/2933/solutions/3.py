def solve(numbers, divisor):
    return [num + num % divisor for num in numbers]
