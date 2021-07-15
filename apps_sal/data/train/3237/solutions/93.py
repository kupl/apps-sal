def even_or_odd(number: int) -> str:
    """Check if number is even or odd. Return 'Even' or 'Odd'"""
    if type(number) is not int:
        print('Argument must be an integer!')
    else:
        return "Even" if number % 2 == 0 else "Odd"

