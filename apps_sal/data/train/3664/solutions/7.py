def cat_mouse(string):
    """Is "m" in jump distance from "C" in 'string'?"""
    return 'Caught!' if abs(string.index('C') - string.index('m')) <= 4 else 'Escaped!'
