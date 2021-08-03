def validate_pin(pin):

    num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    pin_set = set(pin)

    if (len(pin) == 4 or len(pin) == 6) and pin_set.issubset(num):
        return True
    else:
        return False
