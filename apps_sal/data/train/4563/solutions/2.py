tbl = str.maketrans('789456123', '123456789')


def computer_to_phone(numbers):
    return numbers.translate(tbl)
