def bonus_time(s, bonus):
    if bonus == True:
        return '$' + str(s * 10)
    else:
        return '$' + str(s)
