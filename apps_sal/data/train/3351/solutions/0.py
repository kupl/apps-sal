def evil_code_medal(user_time, gold, silver, bronze):
    for (medal, time) in [['Gold', gold], ['Silver', silver], ['Bronze', bronze]]:
        if user_time < time:
            return medal
    return 'None'
