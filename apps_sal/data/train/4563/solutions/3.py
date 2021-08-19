def computer_to_phone(numbers):
    conversion = '0789456123'
    return ''.join([conversion[int(x)] for x in numbers])
