def simple_multiplication(number):
    format_number = int(number)
    result = format_number * 8 if format_number % 2 == 0 else format_number * 9
    return result
