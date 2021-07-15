def signed_eight_bit_number(s):
    try:
        return -128 <= int(s) <= 127 and str(int(s)) == s
    except ValueError:
        return False
