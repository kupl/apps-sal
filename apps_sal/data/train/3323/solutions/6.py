faulty_odometer = lambda n: int(str(n).translate(''.maketrans('56789', '45678')), base = 9)
