def validate_pin(p):
    return p.isdigit() and len(p) in (4, 6)
