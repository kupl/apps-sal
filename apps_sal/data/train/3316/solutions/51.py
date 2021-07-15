def how_many_light_sabers_do_you_own(*name):
    return sum([18 if i == 'Zach' else 0 for i in name])
