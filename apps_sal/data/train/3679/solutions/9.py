def calculate_string(st):
    clean = '+-*/1234567890.'
    st = ''.join([char for char in st if char in clean])
    return str(round(eval(st)))
