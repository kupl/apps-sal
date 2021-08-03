def computer_to_phone(numbers):
    d = {'7': '1', '8': '2', '9': '3', '4': '4', '5': '5', '6': '6', '1': '7', '2': '8', '3': '9', '0': '0'}
    return ''.join([d[c] if c in d else c for c in numbers])
