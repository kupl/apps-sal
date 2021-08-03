def find(n):
    numbers = [number for number in range(1, n + 1) if number % 3 == 0 or number % 5 == 0]
    return sum(numbers)
