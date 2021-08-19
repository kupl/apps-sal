def validate_pin(pin):
    import re
    if len(pin) == 4 or len(pin) == 6:
        if re.search('[^0-9]', pin) == None:
            return True
    return False
