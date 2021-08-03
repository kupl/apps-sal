def string_to_number(s):
    for number in s:
        if number in '+-1234567890':
            return int(s)
