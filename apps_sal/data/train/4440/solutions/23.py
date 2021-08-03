def validate_pin(pin):
    l = len(pin)
    if((l == 4 or l == 6) and pin.isnumeric()):
        return True
    return False
