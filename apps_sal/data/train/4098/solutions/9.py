def new_numeral_system(s):
    n = ord(s)
    return [f'{chr(i + 65)} + {chr(n - i)}' for i in range((n - 65) // 2 + 1)]
