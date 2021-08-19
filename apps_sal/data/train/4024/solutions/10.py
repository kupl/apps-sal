def special_number(number):
    return ['NOT!!', 'Special!!'][all(map(lambda x: x >= 0 and x <= 5, map(int, str(number))))]
