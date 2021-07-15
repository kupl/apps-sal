def validate_pin(pin):
    return pin.isdigit() and len(str(pin)) in [4, 6]
