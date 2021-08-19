def plane_seat(a):
    try:
        (number, letter) = (a[:-1], a[-1])
        number = int(number)
        if not 1 <= number <= 60 or not letter in 'ABCDEFGHK':
            return 'No Seat!!'
        result = []
        return '-'.join(('Front' if number <= 20 else 'Middle' if number <= 40 else 'Back', 'Left' if letter in 'ABC' else 'Middle' if letter in 'DEF' else 'Right'))
    except:
        return 'No Seat!!'
