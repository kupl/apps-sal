def validate_pin(pin):
    return pin.isdecimal() and len(pin) in (4,6)
