def faulty_odometer(n): return int(str(n).translate(''.maketrans('56789', '45678')), base=9)
