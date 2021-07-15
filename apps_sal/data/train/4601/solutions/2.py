from math import log, ceil
def mormons(starting_number, reach, target):
    return ceil( log(target/starting_number) / log(1+reach) )
