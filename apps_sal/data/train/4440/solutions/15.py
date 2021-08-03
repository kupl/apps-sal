def validate_pin(pin):

    if (type(pin) == int or str(pin).isdigit() == True) and (len(str(pin)) == 6 or len(str(pin)) == 4):
        return True
    else:
        return False
