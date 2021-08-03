def sillycase(silly):
    n = len(silly) >> 1
    if ~len(silly) & 1:
        return silly[:n].lower() + silly[n:].upper()
    return silly[:n + 1].lower() + silly[n + 1:].upper()
