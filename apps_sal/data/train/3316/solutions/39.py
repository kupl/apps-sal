def how_many_light_sabers_do_you_own(*name):
    res = list(name)
    try:
        return 18 if res[0] == 'Zach' else 0
    except:
        return 0
