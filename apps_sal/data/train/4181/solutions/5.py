def filter_numbers(string):
    numbers="1234567890"
    return "".join(x for x in string if x not in numbers)
