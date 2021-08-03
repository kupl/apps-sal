def sillycase(silly):
    return silly[:(len(silly) + 1) // 2].lower() + silly[(len(silly) + 1) // 2:].upper()
