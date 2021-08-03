def signed_eight_bit_number(number):
    return number in list(map(str, list(range(-128, 128))))
