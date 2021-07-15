def divisible_by(numbers, divisor):
    """
        Returns all numbers which are divisible by 'divisor'.
    """
    return [number for number in numbers if not number % divisor]
