import re

# Assigning default empty value if no name is entered.
# When not done, Exit code is non-zero with a TypeError - missing 1 required positional argument: 'name'
# if the function is called without argument.


def how_many_light_sabers_do_you_own(name=''):
    # Return 18 if you match Zach, in all other cases, return 0
    return 18 if re.match('^Zach$', name) else 0
