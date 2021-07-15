def how_many_light_sabers_do_you_own(name="null"):
    try:
        if name=="Zach":
            return 18
        else:
            return 0
    except TypeError:
        return 0
