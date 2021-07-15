import re

def power_of_two(x):
    return True if re.match(r"^1[0]*$", bin(x)[2:]) else False

