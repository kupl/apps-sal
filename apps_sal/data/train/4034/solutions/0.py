def sillycase(silly):
    half = (len(silly) + 1) // 2
    return silly[:half].lower() + silly[half:].upper()
