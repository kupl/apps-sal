tr=str.maketrans('56789','45678')

def faulty_odometer(n):
    return int(str(n).translate(tr),9)
