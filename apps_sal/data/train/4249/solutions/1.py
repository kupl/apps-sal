def base64_to_base10(strr):
    return int(''.join([('0' * 6 + bin('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'.index(c))[2:])[-6:] for c in strr]), 2)
