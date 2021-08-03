def get_issuer(number):
    num_string = str(number)
    if num_string[:2] == '34' or num_string[:2] == '37':
        if len(num_string) == 15:
            return 'AMEX'
    if num_string[:4] == '6011' and len(num_string) == 16:
        return 'Discover'
    if int(num_string[:2]) in range(51, 56):
        if len(num_string) == 16:
            return 'Mastercard'
    if num_string[:1] == '4':
        if len(num_string) == 13 or len(num_string) == 16:
            return 'VISA'
    return 'Unknown'
