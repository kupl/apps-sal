def validate_code(code):
    wert = str(code)
    print(wert)
    if wert[0] == '1':
        return True
    elif wert[0] == '2':
        return True
    elif wert[0] == '3':
        return True
    else:
        return False
