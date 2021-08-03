def how_many_light_sabers_do_you_own(*name):
    if len(name) == 0:
        return 0
    return 18 if name[0] == 'Zach' else 0
