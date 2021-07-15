def how_many_light_sabers_do_you_own(name=''):
    switch = {      
        'Zach':  18,
        }
    return switch.get(name, 0)
