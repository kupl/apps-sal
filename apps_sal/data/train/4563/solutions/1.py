def computer_to_phone(numbers):
    return numbers.translate(str.maketrans('123789', '789123'))
