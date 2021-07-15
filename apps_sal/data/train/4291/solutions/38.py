def century(year):
    digits = list(str(year).zfill(6))
    century = int("".join(digits[0:4]))
    years = "".join(digits[4:7])
    if years == "00":
        return century
    else:
        return century + 1


