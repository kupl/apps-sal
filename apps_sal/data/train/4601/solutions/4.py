import math
def mormons(starting_number, reach, target):
    return math.ceil(math.log(target/starting_number,reach+1))
