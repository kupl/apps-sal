def switch_it_up(number):
    numbers = 'Zero-One-Two-Three-Four-Five-Six-Seven-Eight-Nine'.split('-')
    return numbers[number] if number < len(numbers) else 'Error'
