def new_numeral_system(number):
    n = ord(number) - 65
    return [f'{chr(x + 65)} + {chr(n - x + 65)}' for x in range(0, n // 2 + 1)]
