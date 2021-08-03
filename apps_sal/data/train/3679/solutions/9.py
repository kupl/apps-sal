def calculate_string(st):
    clean = '+-*/1234567890.'  # input of acceptable chars
    st = ''.join([char for char in st if char in clean])  # clean the input string
    return str(round(eval((st))))  # evaluate input before rounding and returning as string
