def validate_pin(pin):
    return all((pin.isdigit(), len(pin)==4 or len(pin)==6))
