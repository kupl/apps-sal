def plane_seat(a):
    num, alpha = int(a[:-1]), a[-1]
    if num > 60 or alpha in 'IJ' or alpha > 'K':
        return 'No Seat!!'
    section = ('Front', 'Middle', 'Back')[(num > 20) + (num > 40)]
    cluster = ('Left', 'Middle', 'Right')[(alpha > 'C') + (alpha > 'F')]
    return f'{section}-{cluster}'
