def validate_pin(pin):
    if len(pin) != 4 and len(pin) != 6 or pin.isdigit() == False:
        code = False
    else:
        code = True
    return code
