import math

def sillycase(silly):
    if len(silly) % 2 == 0:
        even_half = len(silly) // 2
        return silly[:even_half].lower() + silly[even_half:].upper()
    else:
        odd_half = math.ceil(len(silly) / 2)
        return silly[:odd_half].lower() + silly[odd_half:].upper()
