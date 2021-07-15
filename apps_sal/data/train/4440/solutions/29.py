def validate_pin(num):
    return True if len(num) in [4,6] and num.isdigit() else False
