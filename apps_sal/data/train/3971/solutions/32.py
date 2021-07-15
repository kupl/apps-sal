def tidyNumber(n):
    for i, digit in enumerate(str(n)[1:]):
        if int(digit) >= int(str(n)[i]):
            pass
        else:
            return False
    return True
