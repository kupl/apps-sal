def hex_to_dec(s):
    r_number = 0
    for idx, letter in enumerate(s.upper()[::-1]):
        if ord(letter) >= 65 and ord(letter) <= 70:
            r_number += (ord(letter) - 55) * (16**idx)
        elif ord(letter) >= 48 and ord(letter) <= 57:
            r_number += (ord(letter) - 48) * (16**idx)
        else:
            print('not a proper hex number :', letter)
            return
    return r_number
