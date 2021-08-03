def faulty_odometer(n): return int(str(n).translate(str.maketrans('56789', '45678')), 9)
