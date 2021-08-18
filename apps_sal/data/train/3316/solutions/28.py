import re


def how_many_light_sabers_do_you_own(name=''):
    return 18 if re.match('^Zach$', name) else 0
