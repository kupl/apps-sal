def find_digit(BLM, BlM):
    if BlM <= 0:
        return -1
    return 0 if BlM > len(str(BLM)) else int(str(BLM)[::-1][BlM - 1])
