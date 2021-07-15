def unused_digits(*args):
    return "".join(number for number in "0123456789" if number not in str(args))
