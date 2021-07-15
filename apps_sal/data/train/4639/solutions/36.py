def power_of_two(x):
    import re
    pattern = re.compile('^0b10*$')
    return re.match(pattern, bin(x)) is not None
