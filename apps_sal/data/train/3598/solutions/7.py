def plane_seat(a):
    (n, l) = (int(a[:-1]), a[-1])
    if n > 60 or l not in 'ABCDEFGHK':
        return 'No Seat!!'
    n = 'Front' if n < 21 else 'Middle' if n < 40 else 'Back'
    l = 'Left' if l < 'D' else 'Middle' if l < 'G' else 'Right'
    return '{}-{}'.format(n, l)
