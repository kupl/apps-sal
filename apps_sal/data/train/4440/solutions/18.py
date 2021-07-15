def validate_pin(pin):
    return {
        6: True if [1 for x in pin if x.isdigit()].count(1) == 6 and len(pin) == 6 else False,
        4: True if [1 for x in pin if x.isdigit()].count(1) == 4 and len(pin) == 4 else False,
    }.get(len(pin), False)
