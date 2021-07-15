import math
def sillycase(silly):
    first = silly[:math.ceil(len(silly) / 2)].lower()
    last = silly[math.ceil(len(silly) / 2):].upper()
    return first + last

    

