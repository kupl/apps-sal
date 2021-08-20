from re import compile
p = compile('\\A(\\d{4}|\\d{6})\\Z')


def validate_pin(pin):
    return bool(p.match(pin))
