def special_number(number):
    return ('Special!!', 'NOT!!')[max(str(number)) > '5']
