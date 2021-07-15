def signed_eight_bit_number(number):
    try:
        i = int(number)
        return (-128 <= i <= 127) and number == str(i)
    except:
        pass
    return False

