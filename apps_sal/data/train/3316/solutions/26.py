def how_many_light_sabers_do_you_own(name=None):
    try:
        return 18 if name=='Zach'else 0
    except AttributeError:
        return 0
