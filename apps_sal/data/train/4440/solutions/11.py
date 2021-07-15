def validate_pin(pin):
    if(len(pin) != 4 and len(pin) != 6):
        return False
    for i in range(len(pin)):
        try:
            int(pin[i])
            if(i == len(pin) - 1):
                return True
        except ValueError:
            break
    return False
