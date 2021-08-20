def rain_amount(mm):
    more = 'You need to give your plant {amount}mm of water'.format(amount=40 - mm)
    enough = 'Your plant has had more than enough water for today!'
    return more if mm < 40 else enough
