def how_many_light_sabers_do_you_own(*name):
    try:
        name = list(name)
        if name is []:
            name.append("")

        return 18 if str(name[0]) == "Zach" else 0
    except:
        return 0
