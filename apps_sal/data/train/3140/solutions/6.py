def happy_number(number):
    if number == 7 or number == 1:
        return True
    while number >= 10:
        number = sum((int(x) ** 2 for x in str(number)))
    if number == 1 or number == 7:
        return True
    else:
        return False


print(happy_number(1112))


def happy_numbers(limit):
    return [number for number in range(1, limit + 1) if happy_number(number)]
