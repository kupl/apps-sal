def rain_amount(mm):
    return ('Your plant has had more than enough water for today!', 'You need to give your plant %dmm of water' % (40 - mm))[mm < 40]
