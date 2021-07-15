from math import ceil
def sillycase(silly):
    return silly[:ceil(len(silly)/2)].lower() + silly[ceil(len(silly)/2):].upper()
