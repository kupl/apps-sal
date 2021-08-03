from re import compile

p = compile(r"\A(\d{4}|\d{6})\Z")


def validate_pin(pin):
    return bool(p.match(pin))
