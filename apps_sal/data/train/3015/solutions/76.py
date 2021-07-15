def get_issuer(number):
    AMEX_FIRST_DIGITS = ('34', '37')
    DISCOVER_FIRST_DIGITS = ('6011')
    MASTERCARD_FIRST_DIGITS = ('51', '52', '53', '54', '55')
    VISA_FIRST_DIGITS = ('4')
    
    number = str(number)
    if number.startswith(AMEX_FIRST_DIGITS) and len(number) == 15:
        return "AMEX"
    elif number.startswith(DISCOVER_FIRST_DIGITS) and len(number) == 16:
        return "Discover"
    elif number.startswith(MASTERCARD_FIRST_DIGITS) and len(number) == 16:
        return "Mastercard"
    elif number.startswith(VISA_FIRST_DIGITS) and len(number) in (13, 16):
        return "VISA"
    else:
        return 'Unknown'
    

