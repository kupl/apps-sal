faulty_odometer = lambda n: int(str(n).translate(str.maketrans('56789', '45678')), 9)
