def calculate_string(st):
    return str(round(eval(''.join((a for a in st if a in '0123456789.+-*/')))))
