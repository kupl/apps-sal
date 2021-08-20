def rain_amount(mm):
    if mm < 40:
        sum = mm - 40
        return 'You need to give your plant ' + str(abs(sum)) + 'mm of water'
    else:
        return 'Your plant has had more than enough water for today!'
