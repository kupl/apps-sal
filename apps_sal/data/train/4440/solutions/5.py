def validate_pin(pin):
    import re
    if len(pin) == 4 or len(pin) == 6:  # not 4 or 6 digits
        if re.search('[^0-9]', pin) == None:  # contains non-digit chars
            return True

    return False
