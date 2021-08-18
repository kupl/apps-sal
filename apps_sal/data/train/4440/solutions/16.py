def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        forbiden = "., ' /\n = -`~!@
        for i in forbiden:
            if i in pin:
                return False
        return True
    else:
        return False
