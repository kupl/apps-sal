def get_column_title(number):
    if number <= 0: raise ValueError
    if number <= 26: return chr(number + 64)
    else: return get_column_title((number-1) // 26) + chr(65 + (number-1) % 26)
