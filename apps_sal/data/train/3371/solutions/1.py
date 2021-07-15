def signed_eight_bit_number(number):
    if number in list(map(str,list(range(-128,128)))):
        return True
    return False
        

