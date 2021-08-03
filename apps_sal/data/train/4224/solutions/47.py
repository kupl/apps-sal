def dont_give_me_five(start: int, end: int):

    list_of_numbers = range(start, end + 1)

    range_without_fives = []

    for number in list_of_numbers:
        digits_list = list(str(number))
        if '5' not in digits_list:
            range_without_fives.append(int(''.join(str(digit) for digit in digits_list)))

    return len(range_without_fives)
