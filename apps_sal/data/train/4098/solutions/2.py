def new_numeral_system(number):
    return [chr(65 + i) + ' + ' + chr(ord(number) - i) for i in range((ord(number) - 65) // 2 + 1)]
