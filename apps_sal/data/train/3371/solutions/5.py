import re
def signed_eight_bit_number(n):
    return re.match(r'-?\d+$',n)and str(int(n))==n and -128<=int(n)<128 or False
