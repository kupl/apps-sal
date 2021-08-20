digits = [str(n) for n in range(10)]


def validate_pin(pin):
    return (len(pin) == 4 or len(pin) == 6) and all((p in digits for p in pin))
