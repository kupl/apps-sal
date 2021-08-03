def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isnumeric() == True:
            return True
        else:
            return False
    else:
        return False
