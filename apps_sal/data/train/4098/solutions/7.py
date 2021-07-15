def new_numeral_system(letter):
    number = ord(letter) - 65
    half = number // 2
    return [f"{chr(i+65)} + {chr(number-i+65)}" for i in range(half + 1)]
