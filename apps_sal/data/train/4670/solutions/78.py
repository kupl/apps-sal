def string_to_number(s):
    try:
        return int(s)
    except ValueError:
        print('Input data cannot be represented as a number')
        return None
