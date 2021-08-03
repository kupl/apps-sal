def how_many_light_sabers_do_you_own(*name):
    try:
        name
    except NameError:
        return 0
    else:
        if 'Zach' in name:
            return 18
        return 0
